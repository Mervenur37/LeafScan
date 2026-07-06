"""
tedavi_kontrol.py
-----------------
class_names.json içindeki 38 sınıfı tek tek gezer ve her biri için
hastalik_bilgi sözlüğünde açıklama + tedavi önerisi olup olmadığını kontrol eder.
Eksik (boş dönen) hastalıkları listeler.

Çalıştırmak için: backend klasöründe   python tedavi_kontrol.py
"""

import json
import os

# app.py ile aynı klasör yapısını kullanıyoruz
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, '..', 'bitki_projesi_model')

# app.py'deki sözlük ve fonksiyonu buraya import ediyoruz
# (app.py aynı klasörde olduğu için doğrudan import edebiliriz)
from app import _translate_class_name, _load_class_names

def main():
    # 38 sınıfı yükle: {index: "Apple___Black_rot", ...}
    class_names = _load_class_names()

    eksikler = []   # tedavi önerisi boş olan sınıflar
    dolular = []    # tedavi önerisi olan sınıflar

    # Her sınıfı tek tek kontrol et
    for idx in sorted(class_names.keys()):
        cn = class_names[idx]  # örn: "Apple___Black_rot"
        plant_tr, plant_en, disease_tr, disease_en, is_healthy, description, recommendation = _translate_class_name(cn)

        # Sağlıklı sınıfları atlıyoruz (onların tedavisi zaten yok, normal)
        if is_healthy:
            continue

        # Açıklama VEYA öneri boşsa, bu sınıf eksik demektir
        if description == '' or recommendation == '':
            eksikler.append((cn, plant_tr, disease_tr))
        else:
            dolular.append((cn, plant_tr, disease_tr))

    # --- Sonuçları yazdır ---
    print(f"\n{'='*60}")
    print(f"TOPLAM HASTALIKLI SINIF: {len(eksikler) + len(dolular)}")
    print(f"  Tedavi önerisi DOLU : {len(dolular)}")
    print(f"  Tedavi önerisi EKSİK: {len(eksikler)}")
    print(f"{'='*60}\n")

    if eksikler:
        print("EKSİK OLANLAR (bunlara açıklama/öneri eklemeliyiz):\n")
        for cn, plant, disease in eksikler:
            print(f"  - {cn}")
            print(f"      Bitki: {plant}  |  Hastalik: {disease}")
    else:
        print("Tebrikler! Tüm hastalıklı sınıfların tedavi önerisi var.")

    print()

if __name__ == '__main__':
    main()
