"""
Bitki Hastalığı Tespit API
Flask backend for plant disease detection using trained CNN models.
"""

import os
# Keras 3.x hatasını önlemek için eski keras 2 modunu aktifleştir
os.environ['TF_USE_LEGACY_KERAS'] = '1'
import json
import numpy as np
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import io
import tensorflow as tf
import keras

# Sohbet asistanı için Gemini
import google.generativeai as genai

# Hastalık bilgi sözlüğü ayrı bir dosyada tutuluyor (belirtiler, organik/kimyasal tedavi, önleme)
from hastalik_bilgi import hastalik_bilgi

# ---------------------------------------------------------------------------
# Ortam değişkenleri ve Gemini yapılandırması
# ---------------------------------------------------------------------------
from config import GEMINI_API_KEY
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# Asistanın kişiliği ve sınırları (system prompt)
CHAT_SYSTEM_PROMPT = """Sen LeafScan adlı bir bitki hastalığı tespit uygulamasının yardımcı asistanısın.
Görevin, kullanıcılara bitki hastalıkları, tedavi yöntemleri, önleme ve bitki bakımı konularında
Türkçe, anlaşılır ve pratik cevaplar vermek.

Kurallar:
- Sadece bitki, tarım, bahçecilik ve bitki hastalıkları konularında yardım et.
- Konu dışı sorulara (kişisel, siyasi, alakasız) kibarca "Ben sadece bitki ve hastalıkları
  konusunda yardımcı olabilirim" diyerek yönlendir.
- Cevapların kısa, net ve uygulanabilir olsun.
- Kesin tıbbi/kimyasal doz vermek yerine genel öneriler sun; ciddi durumlarda bir ziraat
  uzmanına danışılmasını öner.
"""

# ---------------------------------------------------------------------------
# App configuration
# ---------------------------------------------------------------------------
app = Flask(__name__)
CORS(app)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, '..', 'bitki_projesi_model')

# ---------------------------------------------------------------------------
# Lazy model cache
# ---------------------------------------------------------------------------
_model_cache = {}

AVAILABLE_MODELS = ['best_model', 'best_model_v2', 'best_model_v3', 'best_model_v4', 'best_model_v5', 'best_model_v6']

bitki_isimleri = {
    "Apple": "Elma",
    "Blueberry": "Yaban Mersini",
    "Cherry_(including_sour)": "Kiraz",
    "Corn_(maize)": "Mısır",
    "Grape": "Üzüm",
    "Orange": "Portakal",
    "Peach": "Şeftali",
    "Pepper,_bell": "Biber",
    "Potato": "Patates",
    "Raspberry": "Ahududu",
    "Soybean": "Soya Fasulyesi",
    "Squash": "Kabak",
    "Strawberry": "Çilek",
    "Tomato": "Domates",
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _load_class_names():
    """Load class names from the JSON file. Returns {index: class_name} dict."""
    path = os.path.join(MODEL_DIR, 'class_names.json')
    with open(path, 'r', encoding='utf-8') as f:
        raw = json.load(f)
    return {v: k for k, v in raw.items()}


def _get_model(model_name: str):
    """Lazy-load a Keras model and cache it."""
    if model_name in _model_cache:
        return _model_cache[model_name]

    model_path = os.path.join(MODEL_DIR, f'{model_name}.keras')
    if not os.path.exists(model_path):
        return None

    model = keras.models.load_model(
        model_path,
        compile=False,
        custom_objects={'Functional': keras.models.Model},
        safe_mode=False
    )
    _model_cache[model_name] = model
    return model


def _bos_bilgi(disease_tr):
    """Sözlükte bulunamayan hastalıklar için boş bir bilgi yapısı döndürür."""
    return {
        "hastalik_tr": disease_tr,
        "belirtiler": "",
        "organik_tedavi": "",
        "kimyasal_tedavi": "",
        "onleme": "",
    }


def _translate_class_name(class_name_en: str):
    """
    Parse an English class name like 'Apple___Black_rot' and return
    (plant_tr, plant_en, disease_tr, disease_en, is_healthy, info).
    """
    parts = class_name_en.split('___')
    plant_en = parts[0] if len(parts) > 0 else class_name_en
    disease_en = parts[1] if len(parts) > 1 else 'healthy'

    plant_tr = bitki_isimleri.get(plant_en, plant_en)

    disease_key = disease_en.replace(' ', '_')

    info = hastalik_bilgi.get(disease_key)
    if info is None:
        for key in hastalik_bilgi:
            if key.lower() in disease_key.lower() or disease_key.lower() in key.lower():
                info = hastalik_bilgi[key]
                break

    is_healthy = 'healthy' in disease_en.lower()

    if info:
        disease_tr = info["hastalik_tr"]
    else:
        disease_tr = 'Sağlıklı' if is_healthy else disease_en
        info = _bos_bilgi(disease_tr)

    return plant_tr, plant_en, disease_tr, disease_en, is_healthy, info


def _translate_class_name_short(class_name_en: str) -> str:
    """Return a short Turkish translation of the class name: 'Bitki - Hastalık'."""
    plant_tr, _, disease_tr, _, is_healthy, _ = _translate_class_name(class_name_en)
    if is_healthy:
        return f"{plant_tr} - Sağlıklı"
    return f"{plant_tr} - {disease_tr}"


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})


@app.route('/api/classes', methods=['GET'])
def get_classes():
    try:
        class_names = _load_class_names()
        classes = []
        for idx in sorted(class_names.keys()):
            cn = class_names[idx]
            plant_tr, plant_en, disease_tr, disease_en, is_healthy, info = _translate_class_name(cn)
            classes.append({
                'index': idx,
                'class_name': cn,
                'class_name_tr': _translate_class_name_short(cn),
                'plant': plant_tr,
                'plant_en': plant_en,
                'disease': disease_tr,
                'disease_en': disease_en,
                'is_healthy': is_healthy,
            })
        return jsonify({'classes': classes, 'count': len(classes)})
    except FileNotFoundError:
        return jsonify({'error': 'class_names.json bulunamadı'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/models', methods=['GET'])
def get_models():
    models = []
    for name in AVAILABLE_MODELS:
        path = os.path.join(MODEL_DIR, f'{name}.keras')
        models.append({
            'name': name,
            'exists': os.path.exists(path),
        })
    return jsonify({'models': models})


@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'Görüntü dosyası gerekli (image alanı)'}), 400

        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'Dosya seçilmedi'}), 400

        model_name = request.form.get('model', 'best_model_v4')
        if model_name not in AVAILABLE_MODELS:
            return jsonify({'error': f'Geçersiz model adı. Mevcut modeller: {AVAILABLE_MODELS}'}), 400

        model = _get_model(model_name)
        if model is None:
            return jsonify({'error': f'Model dosyası bulunamadı: {model_name}.keras'}), 404

        class_names = _load_class_names()

        image_bytes = file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
        image = image.resize((128, 128))
        img_array = np.array(image, dtype=np.float32) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        predictions = model.predict(img_array, verbose=0)[0]

        top_indices = np.argsort(predictions)[::-1][:5]
        top_predictions = []
        for idx in top_indices:
            cn = class_names[idx]
            top_predictions.append({
                'class_name': _translate_class_name_short(cn),
                'class_name_en': cn,
                'confidence': round(float(predictions[idx]) * 100, 2),
            })

        best_idx = top_indices[0]
        best_class = class_names[best_idx]
        plant_tr, plant_en, disease_tr, disease_en, is_healthy, info = _translate_class_name(best_class)

        return jsonify({
            'plant': plant_tr,
            'plant_en': plant_en,
            'disease': disease_tr,
            'disease_en': disease_en,
            'is_healthy': is_healthy,
            'confidence': round(float(predictions[best_idx]) * 100, 2),
            'description': info.get('belirtiler', ''),
            'recommendation': info.get('organik_tedavi', ''),
            'belirtiler': info.get('belirtiler', ''),
            'organik_tedavi': info.get('organik_tedavi', ''),
            'kimyasal_tedavi': info.get('kimyasal_tedavi', ''),
            'onleme': info.get('onleme', ''),
            'top_predictions': top_predictions,
            'model_used': model_name,
        })

    except Exception as e:
        return jsonify({'error': f'Tahmin sırasında hata oluştu: {str(e)}'}), 500


@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        if not GEMINI_API_KEY:
            return jsonify({'error': 'Sohbet servisi yapılandırılmamış (API anahtarı eksik).'}), 503

        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'error': 'Mesaj gerekli.'}), 400

        user_message = data['message']
        disease_context = data.get('disease_context', '')

        if disease_context:
            full_message = f"[Tespit edilen hastalık: {disease_context}]\n\nKullanıcı sorusu: {user_message}"
        else:
            full_message = user_message

        model = genai.GenerativeModel(
            model_name='gemini-2.5-flash',
            system_instruction=CHAT_SYSTEM_PROMPT
        )

        response = model.generate_content(full_message)

        return jsonify({'reply': response.text})

    except Exception as e:
        return jsonify({'error': f'Sohbet sırasında hata oluştu: {str(e)}'}), 500


@app.route('/api/metrics', methods=['GET'])
def get_metrics():
    cache_path = os.path.join(BASE_DIR, 'metrics_cache.json')
    if not os.path.exists(cache_path):
        return jsonify({
            'status': 'not_ready',
            'message': 'Metrikler henüz hesaplanmadı. evaluate_models.py scriptini çalıştırın.',
        })
    try:
        with open(cache_path, 'r', encoding='utf-8') as f:
            metrics = json.load(f)
        return jsonify(metrics)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/metrics/<model_name>', methods=['GET'])
def get_model_metrics(model_name):
    cache_path = os.path.join(BASE_DIR, 'metrics_cache.json')
    if not os.path.exists(cache_path):
        return jsonify({
            'status': 'not_ready',
            'message': 'Metrikler henüz hesaplanmadı. evaluate_models.py scriptini çalıştırın.',
        })
    try:
        with open(cache_path, 'r', encoding='utf-8') as f:
            metrics = json.load(f)

        if model_name not in metrics.get('models', {}):
            available = list(metrics.get('models', {}).keys())
            return jsonify({'error': f'Model bulunamadı: {model_name}. Mevcut modeller: {available}'}), 404

        model_metrics = metrics['models'][model_name]
        return jsonify({
            'model_name': model_name,
            'evaluation_date': metrics.get('evaluation_date'),
            'dataset': metrics.get('dataset'),
            'num_classes': metrics.get('num_classes'),
            'class_names': metrics.get('class_names'),
            'class_names_tr': metrics.get('class_names_tr'),
            **model_metrics,
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True, port=5000)