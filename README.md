# 🌿 LeafScan — Plant Disease Detection

An AI-powered plant disease detection system. Upload a leaf photo to find out the plant species and its disease.

*(Türkçe versiyon için aşağı kaydırın / Scroll down for Turkish version)*

## 📋 About the Project

This project is a deep learning-based plant disease detection application. The models, trained using the MobileNetV2 architecture and transfer learning, can recognize 38 disease classes across 14 different plants.

### Features

- 🔬 **Leaf Analysis:** Upload a leaf photo to detect the plant species and disease
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
                                    ┌──────────┴─────────┐
                                    │  Keras Models       │
                                    │  (MobileNetV2)      │
                                    └────────────────────┘
```

### Technology Stack

| Layer | Technology |
|--------|-----------|
| **Frontend** | React 19, Vite, Recharts, Framer Motion, Lucide Icons, html2canvas, jsPDF |
| **Backend** | Flask, Flask-CORS |
| **Model** | TensorFlow/Keras, MobileNetV2 (Transfer Learning) |
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

After downloading, extract the contents into the `bitki_projesi/bitki_projesi_model/` folder. The folder should contain the `.keras` model files and the `.pkl` helper files.

### 3. Backend Setup

```bash
cd backend
pip install -r requirements.txt
```

### 4. Frontend Setup

```bash
cd ../frontend
npm install
```

## ▶️ Running the App

### 1. Start Backend

```bash
cd backend
python app.py
```

Backend runs at http://localhost:5000.

### 2. Start Frontend

Open a new terminal:

```bash
cd frontend
npm run dev
```

Frontend runs at http://localhost:5173.

### 3. Open in Browser

Go to http://localhost:5173.

## 📖 Usage

### Leaf Analysis

1. Click "Analizi Başlat" on the landing page
2. Upload a leaf photo (drag & drop or click)
3. Optionally crop the image using the scissors icon for better accuracy
4. Results appear automatically:
   - Plant species
   - Disease name (if any)
   - Model confidence score (%)
   - Top 5 predictions
   - Disease description and treatment recommendation
5. Save results as PDF using the "PDF Kaydet" button

### Model Metrics

Click "Metrikler" in the navbar to access detailed performance analysis:

- **General Metrics:** Accuracy, Precision, Recall, F1-Score, WMAPE, AUC cards
- **Confusion Matrix:** 38×38 interactive heatmap
- **ROC Curve:** Multi-class ROC curves and AUC values
- **Class-based Table:** Sortable and filterable performance table
- **Error Analysis:** Class-based error rate chart (WMAPE)

## 🔌 API Documentation

| Endpoint | Method | Description |
|----------|--------|----------|
| `/api/health` | GET | Health check |
| `/api/predict` | POST | Upload image → get prediction |
| `/api/classes` | GET | Supported class list |
| `/api/models` | GET | Available model list |
| `/api/metrics` | GET | Metrics of all models |
| `/api/metrics/<model>` | GET | Metrics of a single model |

### Predict API Example

```bash
curl -X POST -F "image=@leaf.jpg" -F "model=best_model_v6" http://localhost:5000/api/predict
```

## 📁 Project Structure

```text
bitki_projesi/
├── backend/
│   ├── app.py                 # Flask API server
│   ├── evaluate_models.py     # Model evaluation script
│   ├── requirements.txt       # Python dependencies
│   └── metrics_cache.json     # Calculated metrics (auto-generated)
├── frontend/
│   ├── src/
│   │   ├── components/        # React components
│   │   ├── pages/
│   │   │   ├── LandingPage.jsx
│   │   │   ├── AnalysisPage.jsx
│   │   │   └── MetricsPage.jsx
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── index.css
│   ├── package.json
│   └── vite.config.js
└── bitki_projesi_model/
    ├── best_model_v6.keras    # Active model (default, downloaded from Releases)
    └── class_names.json       # 38 class labels
```

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

### Dataset
- **PlantVillage Dataset:** 38 classes, ~54,000 images
- **PlantDoc Dataset:** Real-world field images, 28 classes mapped
- **Train/Test Split:** 80% train, 20% test (stratified)

## ⚠️ Known Limitations & Future Work

### Known Limitations
- **Out-of-distribution inputs:** The model is trained only on leaf images. When given non-leaf inputs (e.g. cartoons, objects, random photos), it still forces a prediction into one of the 38 disease classes instead of rejecting the input. A low confidence score is often a hint, but the model does not yet say "this is not a leaf."
- **Real-world variance:** Accuracy is highest on clean, centered leaf photos. Complex backgrounds, poor lighting, or multiple leaves in one frame can reduce reliability.

### Future Work
- 🔍 Add a "is this a leaf?" pre-check (confidence threshold or a separate leaf/not-leaf classifier) to reject out-of-distribution inputs
- 💬 Add an LLM-based chat assistant so users can ask follow-up questions about the detected disease
- 🩺 Expand treatment recommendations for each disease
- 📈 Add disease-progress tracking over time for the same plant
- 🎯 Explore segmentation to highlight the exact affected region on the leaf

## 📄 License

This project was developed for educational purposes.

---

*LeafScan · MobileNetV2 + Transfer Learning · PlantVillage + PlantDoc Dataset · 2026*

---

# 🌿 LeafScan — Bitki Hastalığı Tespiti

Yapay zeka destekli bitki hastalığı tespit sistemi. Yaprak fotoğrafı yükleyin, bitkinin türünü ve hastalığını öğrenin.

## 📋 Proje Hakkında

MobileNetV2 mimarisi ve transfer learning kullanılarak eğitilmiş modeller, 14 farklı bitkiye ait 38 hastalık sınıfını tanıyabilmektedir.

### Özellikler

- 🔬 **Yaprak Analizi:** Yaprak fotoğrafı yükleyerek bitkinin türünü ve hastalığını tespit edin
- ✂️ **Kırpma Aracı:** Daha iyi doğruluk için yaprak alanını kırpın
- 💾 **PDF Dışa Aktarma:** Analiz sonuçlarını yaprak görseli ile birlikte PDF olarak kaydedin
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
                                    ┌──────────┴─────────┐
                                    │  Keras Modelleri    │
                                    │  (MobileNetV2)      │
                                    └────────────────────┘
```

### Teknoloji Yığını

| Katman | Teknoloji |
|--------|-----------|
| **Frontend** | React 19, Vite, Recharts, Framer Motion, Lucide Icons, html2canvas, jsPDF |
| **Backend** | Flask, Flask-CORS |
| **Model** | TensorFlow/Keras, MobileNetV2 (Transfer Learning) |
| **Veri Seti** | PlantDoc Classification Dataset, PlantVillage Dataset (38 sınıf, ~54.000 görüntü) |
| **Değerlendirme** | scikit-learn |

## 🌱 Desteklenen Bitkiler ve Hastalıklar (38 Sınıf)

| Bitki | Hastalıklar |
|-------|-------------|
| 🍎 Elma | Karaleke, Kara Çürüklük, Sedir Pası, Sağlıklı |
| 🫐 Yaban Mersini | Sağlıklı |
| 🍒 Kiraz | Küllü Mildiyö, Sağlıklı |
| 🌽 Mısır | Cercospora Yaprak Lekesi, Yaygın Pas, Kuzey Yaprak Yanıklığı, Sağlıklı |
| 🍇 Üzüm | Kara Çürüklük, Esca, Yaprak Yanıklığı, Sağlıklı |
| 🍊 Portakal | Huanglongbing |
| 🍑 Şeftali | Bakteriyel Leke, Sağlıklı |
| 🫑 Biber | Bakteriyel Leke, Sağlıklı |
| 🥔 Patates | Erken Yanıklık, Geç Yanıklık, Sağlıklı |
| 🫐 Ahududu | Sağlıklı |
| 🌱 Soya Fasulyesi | Sağlıklı |
| 🎃 Kabak | Küllü Mildiyö |
| 🍓 Çilek | Yaprak Yanması, Sağlıklı |
| 🍅 Domates | Bakteriyel Leke, Erken Yanıklık, Geç Yanıklık, Yaprak Küfü, Septoria, Kırmızı Örümcek, Hedef Leke, Sarı Yaprak Kıvırcıklık Virüsü, Mozaik Virüsü, Sağlıklı |

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

Eğitilmiş model dosyaları (`.keras`, `.pkl`) boyutları nedeniyle repoya dahil edilmemiştir. Releases sayfasından indirin:

➡️ **[model_dosyalari.zip indir (v1.0)](https://github.com/Mervenur37/LeafScan/releases/download/v1.0/model_dosyalari.zip)**

İndirdikten sonra içindekileri `bitki_projesi/bitki_projesi_model/` klasörüne çıkarın. Klasörde `.keras` model dosyaları ve `.pkl` yardımcı dosyaları bulunmalıdır.

### 3. Backend Kurulumu

```bash
cd backend
pip install -r requirements.txt
```

### 4. Frontend Kurulumu

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

### Veri Seti
- **PlantVillage Dataset:** 38 sınıf, ~54.000 görüntü
- **PlantDoc Dataset:** Gerçek tarla görselleri, 28 sınıf eşleştirildi
- **Eğitim/Test Ayrımı:** %80 eğitim, %20 test (stratified)

## ⚠️ Bilinen Kısıtlamalar & Gelecek Planları

### Bilinen Kısıtlamalar
- **Dağıtım dışı girdiler:** Model yalnızca yaprak görselleri üzerinde eğitilmiştir. Yaprak olmayan girdiler verildiğinde (örneğin karikatür, nesne, alakasız fotoğraf), girdiyi reddetmek yerine 38 hastalık sınıfından birine zorla tahmin üretir. Düşük güven skoru genelde bir ipucudur ancak model henüz "bu bir yaprak değil" diyememektedir.
- **Gerçek dünya değişkenliği:** Doğruluk, temiz ve ortalanmış yaprak fotoğraflarında en yüksektir. Karmaşık arka plan, kötü ışık veya tek karede birden fazla yaprak güvenilirliği düşürebilir.

### Gelecek Planları
- 🔍 Dağıtım dışı girdileri reddetmek için "bu bir yaprak mı?" ön kontrolü ekleme (güven eşiği veya ayrı bir yaprak/yaprak-değil sınıflandırıcısı)
- 💬 Kullanıcıların tespit edilen hastalık hakkında soru sorabilmesi için LLM tabanlı sohbet asistanı ekleme
- 🩺 Her hastalık için tedavi önerilerini genişletme
- 📈 Aynı bitki için zaman içinde hastalık ilerlemesi takibi ekleme
- 🎯 Yaprak üzerindeki hastalıklı bölgeyi işaretlemek için segmentasyon araştırması

## 📄 Lisans

Bu proje eğitim amaçlı geliştirilmiştir.

---

*LeafScan · MobileNetV2 + Transfer Learning · PlantVillage + PlantDoc Dataset · 2026*
