# 🌿 LeafScan — Plant Disease Detection

An AI-powered plant disease detection system with an integrated chat assistant. Upload a leaf photo to find out the plant species and its disease, then ask follow-up questions to the built-in AI assistant.

*(Türkçe versiyon için aşağı kaydırın / Scroll down for Turkish version)*

## 📋 About the Project

This project is a deep learning-based plant disease detection application. The models, trained using the MobileNetV2 architecture and transfer learning, can recognize 38 disease classes across 14 different plants. It also features a Gemini-powered chat assistant for plant-care questions.

### Features

- 🔬 **Leaf Analysis:** Upload a leaf photo to detect the plant species and disease
- 🤖 **AI Chat Assistant:** Gemini-powered assistant that answers questions about plant diseases, treatment and care (aware of the detected disease)
- 💊 **Detailed Treatment Info:** Symptoms, organic treatment, chemical treatment and prevention shown in a tabbed panel
- ✂️ **Crop Tool:** Crop the leaf area for better accuracy
- 💾 **PDF Export:** Save analysis results as PDF with the leaf image
- 🕐 **Analysis History:** View last 5 analyses on the page
- 🌙 **Dark/Light Theme:** Toggle between dark and light mode on the landing page
- 📊 **Model Metrics:** Detailed performance metrics such as Accuracy, Precision, Recall, F1-Score, WMAPE, ROC Curve
- 📈 **Visualization:** Confusion Matrix, ROC curve, WMAPE chart, and more

## 🏗️ Architecture

```text
┌──────────────────┐     REST API     ┌──────────────────┐
│   React Frontend │ ◄──────────────► │   Flask Backend   │
│   (Vite :5173)   │                  │   (Python :5000)  │
└──────────────────┘                  └────────┬─────────┘
                                               │
                              ┌────────────────┼────────────────┐
                              │                                 │
                    ┌─────────┴────────┐            ┌───────────┴──────────┐
                    │  Keras Models     │            │   Gemini API          │
                    │  (MobileNetV2)    │            │   (Chat Assistant)    │
                    └──────────────────┘            └──────────────────────┘
```

### Technology Stack

| Layer | Technology |
|--------|-----------|
| **Frontend** | React 19, Vite, Recharts, Framer Motion, Lucide Icons, html2canvas, jsPDF |
| **Backend** | Flask, Flask-CORS |
| **Model** | TensorFlow/Keras, MobileNetV2 (Transfer Learning) |
| **Chat Assistant** | Google Gemini API (gemini-2.5-flash) |
| **Dataset** | PlantDoc Classification Dataset, PlantVillage Dataset (38 classes, ~54,000 images) |
| **Evaluation** | scikit-learn |

## 🌱 Supported Plants and Diseases (38 Classes)

| Plant | Diseases |
|-------|-------------|
| 🍎 Apple | Apple scab, Black rot, Cedar apple rust, Healthy |
| 🫐 Blueberry | Healthy |
| 🍒 Cherry | Powdery mildew, Healthy |
| 🌽 Corn | Cercospora leaf spot, Common rust, Northern Leaf Blight, Healthy |
| 🍇 Grape | Black rot, Esca, Leaf blight, Healthy |
| 🍊 Orange | Huanglongbing |
| 🍑 Peach | Bacterial spot, Healthy |
| 🫑 Pepper | Bacterial spot, Healthy |
| 🥔 Potato | Early blight, Late blight, Healthy |
| 🫐 Raspberry | Healthy |
| 🌱 Soybean | Healthy |
| 🎃 Squash | Powdery mildew |
| 🍓 Strawberry | Leaf scorch, Healthy |
| 🍅 Tomato | Bacterial spot, Early blight, Late blight, Leaf Mold, Septoria leaf spot, Spider mites, Target Spot, Yellow Leaf Curl Virus, Mosaic virus, Healthy |

## 🚀 Installation

### Prerequisites

- Python 3.9+
- Node.js 18+
- npm 9+

### 1. Clone the Repository

```bash
git clone https://github.com/Mervenur37/LeafScan.git
cd LeafScan/bitki_projesi
```

### 2. Download the Model Files

The trained model files (`.keras`, `.pkl`) are not included in the repository due to their size. Download them from the Releases page:

➡️ **[Download model_dosyalari.zip (v1.0)](https://github.com/Mervenur37/LeafScan/releases/download/v1.0/model_dosyalari.zip)**

After downloading, extract the contents into the `bitki_projesi/bitki_projesi_model/` folder.

### 3. Backend Setup

```bash
cd backend
pip install -r requirements.txt
```

### 4. Configure the Chat Assistant (optional)

The chat assistant uses the Google Gemini API. To enable it:

1. Get a free API key from [Google AI Studio](https://aistudio.google.com/apikey).
2. In the `backend` folder, create a file named `config.py` with the following content:

   ```python
   GEMINI_API_KEY = "your_api_key_here"
   ```

3. This file is git-ignored, so your key stays private and is never pushed to GitHub.

> If you skip this step, the app still works — only the chat assistant will be disabled.

### 5. Frontend Setup

```bash
cd ../frontend
npm install
```

## ▶️ Running the App

```bash
# Terminal 1 - Backend
cd backend
python app.py

# Terminal 2 - Frontend
cd frontend
npm run dev
```

Open http://localhost:5173 in your browser.

## 🔌 API Documentation

| Endpoint | Method | Description |
|----------|--------|----------|
| `/api/health` | GET | Health check |
| `/api/predict` | POST | Upload image → get prediction |
| `/api/chat` | POST | Send a message → get AI assistant reply |
| `/api/classes` | GET | Supported class list |
| `/api/models` | GET | Available model list |
| `/api/metrics` | GET | Metrics of all models |
| `/api/metrics/<model>` | GET | Metrics of a single model |

## 🧠 Model Information

### Architecture
- **Base Model:** MobileNetV2 (transfer learning with ImageNet weights)
- **Input Size:** 128×128 pixels, RGB
- **Output:** 38 classes (softmax)
- **Training:** Fine-tuning + data augmentation (PlantVillage + PlantDoc)

### Model Versions

| Model | Val Accuracy | Description |
|-------|-------------|----------|
| v1 - v4 | — | Previous versions |
| v5 | 98.00% | Further fine-tuning |
| **v6** | **98.34%** | **Active — PlantVillage + PlantDoc** |

## ⚠️ Known Limitations & Future Work

### Known Limitations
- **Out-of-distribution inputs:** The model is trained only on leaf images. When given non-leaf inputs (cartoons, objects, random photos), it still forces a prediction into one of the 38 disease classes instead of rejecting the input. A low confidence score is often a hint, but the model does not yet say "this is not a leaf."
- **Real-world variance:** Accuracy is highest on clean, centered leaf photos. Complex backgrounds, poor lighting, or multiple leaves in one frame can reduce reliability.

### Disclaimer
> The treatment recommendations and chat assistant responses are for **general informational purposes only** and do not replace professional agricultural advice. For serious cases, please consult an agricultural specialist.

### Future Work
- 🔍 Add a "is this a leaf?" pre-check to reject out-of-distribution inputs
- 🩺 Expand treatment recommendations for each disease
- 📈 Add disease-progress tracking over time for the same plant
- 🎯 Explore segmentation to highlight the exact affected region on the leaf

## 📄 License

This project was developed for educational purposes.

---

*LeafScan · MobileNetV2 + Transfer Learning · Gemini Chat Assistant · PlantVillage + PlantDoc Dataset · 2026*

---

# 🌿 LeafScan — Bitki Hastalığı Tespiti

Yapay zeka destekli, sohbet asistanı entegre bitki hastalığı tespit sistemi. Yaprak fotoğrafı yükleyin, bitkinin türünü ve hastalığını öğrenin, ardından yerleşik yapay zeka asistanına sorularınızı sorun.

## 📋 Proje Hakkında

MobileNetV2 mimarisi ve transfer learning kullanılarak eğitilmiş modeller, 14 farklı bitkiye ait 38 hastalık sınıfını tanıyabilmektedir. Ayrıca bitki bakımı sorularını yanıtlayan Gemini destekli bir sohbet asistanı içerir.

### Özellikler

- 🔬 **Yaprak Analizi:** Yaprak fotoğrafı yükleyerek bitkinin türünü ve hastalığını tespit edin
- 🤖 **Yapay Zeka Sohbet Asistanı:** Bitki hastalıkları, tedavi ve bakım hakkında soruları yanıtlayan Gemini destekli asistan (tespit edilen hastalığı bilir)
- 💊 **Detaylı Tedavi Bilgisi:** Belirtiler, organik tedavi, kimyasal tedavi ve önleme sekmeli bir panelde gösterilir
- ✂️ **Kırpma Aracı:** Daha iyi doğruluk için yaprak alanını kırpın
- 💾 **PDF Dışa Aktarma:** Analiz sonuçlarını yaprak görseli ile PDF olarak kaydedin
- 🕐 **Analiz Geçmişi:** Son 5 analizi sayfada görüntüleyin
- 🌙 **Koyu/Açık Tema:** Landing page'de tema değiştirin
- 📊 **Model Metrikleri:** Accuracy, Precision, Recall, F1-Score, WMAPE, ROC Curve
- 📈 **Görselleştirme:** Confusion Matrix, ROC eğrisi, WMAPE grafiği

## 🏗️ Mimari

```text
┌──────────────────┐     REST API     ┌──────────────────┐
│   React Frontend │ ◄──────────────► │   Flask Backend   │
│   (Vite :5173)   │                  │   (Python :5000)  │
└──────────────────┘                  └────────┬─────────┘
                                               │
                              ┌────────────────┼────────────────┐
                              │                                 │
                    ┌─────────┴────────┐            ┌───────────┴──────────┐
                    │  Keras Modelleri  │            │   Gemini API          │
                    │  (MobileNetV2)    │            │   (Sohbet Asistanı)   │
                    └──────────────────┘            └──────────────────────┘
```

### Teknoloji Yığını

| Katman | Teknoloji |
|--------|-----------|
| **Frontend** | React 19, Vite, Recharts, Framer Motion, Lucide Icons, html2canvas, jsPDF |
| **Backend** | Flask, Flask-CORS |
| **Model** | TensorFlow/Keras, MobileNetV2 (Transfer Learning) |
| **Sohbet Asistanı** | Google Gemini API (gemini-2.5-flash) |
| **Veri Seti** | PlantDoc Classification Dataset, PlantVillage Dataset (38 sınıf, ~54.000 görüntü) |
| **Değerlendirme** | scikit-learn |

## 🚀 Kurulum

### Gereksinimler

- Python 3.9+
- Node.js 18+
- npm 9+

### 1. Repoyu Klonla

```bash
git clone https://github.com/Mervenur37/LeafScan.git
cd LeafScan/bitki_projesi
```

### 2. Model Dosyalarını İndir

E�itilmiş model dosyaları (`.keras`, `.pkl`) boyutları nedeniyle repoya dahil edilmemiştir. Releases sayfasından indirin:

➡️ **[model_dosyalari.zip indir (v1.0)](https://github.com/Mervenur37/LeafScan/releases/download/v1.0/model_dosyalari.zip)**

İndirdikten sonra içindekileri `bitki_projesi/bitki_projesi_model/` klasörüne çıkarın.

### 3. Backend Kurulumu

```bash
cd backend
pip install -r requirements.txt
```

### 4. Sohbet Asistanını Yapılandır (opsiyonel)

Sohbet asistanı Google Gemini API kullanır. Etkinleştirmek için:

1. [Google AI Studio](https://aistudio.google.com/apikey)'dan ücretsiz bir API anahtarı alın.
2. `backend` klasöründe `config.py` adında bir dosya oluşturun:

   ```python
   GEMINI_API_KEY = "api_anahtariniz_buraya"
   ```

3. Bu dosya git tarafından yok sayılır (`.gitignore`), yani anahtarınız gizli kalır ve GitHub'a gönderilmez.

> Bu adımı atlarsanız uygulama yine çalışır — sadece sohbet asistanı devre dışı kalır.

### 5. Frontend Kurulumu

```bash
cd ../frontend
npm install
```

## ▶️ Çalıştırma

```bash
# Terminal 1 - Backend
cd backend
python app.py

# Terminal 2 - Frontend
cd frontend
npm run dev
```

Tarayıcıda http://localhost:5173 adresine gidin.

## 🧠 Model Bilgileri

### Mimari
- **Temel Model:** MobileNetV2 (ImageNet ağırlıkları ile transfer learning)
- **Giriş Boyutu:** 128×128 piksel, RGB
- **Çıkış:** 38 sınıf (softmax)
- **Eğitim:** Fine-tuning + data augmentation (PlantVillage + PlantDoc)

### Model Versiyonları

| Model | Val Accuracy | Açıklama |
|-------|-------------|----------|
| v1 - v4 | — | Önceki versiyonlar |
| v5 | 98.00% | Fine-tuning |
| **v6** | **98.34%** | **Aktif — PlantVillage + PlantDoc** |

## ⚠️ Bilinen Kısıtlamalar & Gelecek Planları

### Bilinen Kısıtlamalar
- **Dağıtım dışı girdiler:** Model yalnızca yaprak görselleri üzerinde eğitilmiştir. Yaprak olmayan girdiler verildiğinde (karikatür, nesne, alakasız fotoğraf), girdiyi reddetmek yerine 38 hastalık sınıfından birine zorla tahmin üretir. Düşük güven skoru genelde bir ipucudur ancak model henüz "bu bir yaprak değil" diyememektedir.
- **Gerçek dünya değişkenliği:** Doğruluk, temiz ve ortalanmış yaprak fotoğraflarında en yüksektir. Karmaşık arka plan, kötü ışık veya tek karede birden fazla yaprak güvenilirliği düşürebilir.

### Sorumluluk Reddi
> Tedavi önerileri ve sohbet asistanı yanıtları **yalnızca genel bilgilendirme amaçlıdır** ve profesyonel tarım danışmanlığının yerine geçmez. Ciddi durumlarda lütfen bir ziraat uzmanına danışın.

### Gelecek Planları
- 🔍 Dağıtım dışı girdileri reddetmek için "bu bir yaprak mı?" ön kontrolü ekleme
- 🩺 Her hastalık için tedavi önerilerini genişletme
- 📈 Aynı bitki için zaman içinde hastalık ilerlemesi takibi ekleme
- 🎯 Yaprak üzerindeki hastalıklı bölgeyi işaretlemek için segmentasyon araştırması

## 📄 Lisans

Bu proje eğitim amaçlı geliştirilmiştir.

---

*LeafScan · MobileNetV2 + Transfer Learning · Gemini Sohbet Asistanı · PlantVillage + PlantDoc Dataset · 2026*