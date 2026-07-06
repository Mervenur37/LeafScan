# -*- coding: utf-8 -*-
"""
hastalik_bilgi.py
-----------------
Bitki hastalıkları için yapılandırılmış bilgi sözlüğü.
Her hastalık; Türkçe adı, belirtileri, organik tedavi, kimyasal tedavi
ve önleme yöntemleri ile birlikte tutulur.

app.py bu sözlüğü import ederek kullanır:
    from hastalik_bilgi import hastalik_bilgi

Anahtarlar (Early_blight, Apple_scab vb.) app.py'deki eşleştirme
mantığıyla uyumlu olacak şekilde İngilizce tutulmuştur.
"""

hastalik_bilgi = {
    "healthy": {
        "hastalik_tr": "Sağlıklı",
        "belirtiler": "Bu yaprak sağlıklı görünüyor. Herhangi bir hastalık belirtisi tespit edilmedi.",
        "organik_tedavi": "Tedaviye gerek yok. Bitkinin düzenli bakımına devam edin.",
        "kimyasal_tedavi": "Tedaviye gerek yok.",
        "onleme": "Düzenli sulama, dengeli gübreleme ve iyi hava sirkülasyonu ile bitkiyi sağlıklı tutun.",
    },
    "Early_blight": {
        "hastalik_tr": "Erken Yanıklık",
        "belirtiler": "Alt yapraklardan başlayan, iç içe halkalı (hedef tahtası görünümlü) koyu kahverengi lekeler. Lekelerin çevresinde sararma görülür. Alternaria solani mantarı kaynaklıdır ve nemli, sıcak havalarda hızla yayılır.",
        "organik_tedavi": "Etkilenen yaprakları toplayıp imha edin. Neem yağı veya bakır bazlı organik fungisitler uygulayın. Bitki etrafındaki yabani otları temizleyin.",
        "kimyasal_tedavi": "Mancozeb veya klorotalonil içerikli fungisitleri 7-10 gün aralıklarla uygulayın. Etiket dozajına mutlaka uyun.",
        "onleme": "Bitkiler arası mesafeyi açarak hava sirkülasyonunu artırın. Sulamayı sabah yapın ve yaprakları ıslatmaktan kaçının. Ekim nöbeti (rotasyon) uygulayın.",
    },
    "Late_blight": {
        "hastalik_tr": "Geç Yanıklık",
        "belirtiler": "Yapraklarda su emmiş gibi gri-yeşil lekeler, hızla kahverengiye döner. Nemli havada yaprak altında beyaz küf tabakası oluşur. Phytophthora infestans kaynaklıdır ve çok hızlı yayılarak bitkiyi kısa sürede öldürebilir.",
        "organik_tedavi": "Enfekteli yaprak ve bitkileri hemen imha edin (kompost yapmayın). Bakır bazlı organik fungisitler koruyucu olarak uygulanabilir.",
        "kimyasal_tedavi": "Mancozeb, klorotalonil veya metalaksil içerikli fungisitleri hastalık görülür görülmez uygulayın. Yayılım hızlı olduğu için erken müdahale kritiktir.",
        "onleme": "Dayanıklı çeşitler kullanın. Yaprakları ıslatmayan damla sulama tercih edin. Serin ve nemli dönemlerde bitkileri sık kontrol edin.",
    },
    "Leaf_scorch": {
        "hastalik_tr": "Yaprak Yanması",
        "belirtiler": "Yaprak kenarlarından başlayan kahverengileşme ve kuruma. Genellikle su stresi, aşırı güneş veya mantar (Diplocarpon) kaynaklıdır. Çilekte yaygındır.",
        "organik_tedavi": "Etkilenen yaprakları temizleyin. Toprak nemini dengede tutun, malçlama ile nem kaybını azaltın. Neem yağı uygulanabilir.",
        "kimyasal_tedavi": "Mantar kaynaklıysa kaptan veya miklobutanil içerikli fungisit uygulayın.",
        "onleme": "Düzenli ve dengeli sulama yapın. Aşırı gübrelemeden kaçının. İyi drenajlı toprak sağlayın.",
    },
    "Black_rot": {
        "hastalik_tr": "Kara Çürüklük",
        "belirtiler": "Yapraklarda kahverengi lekeler ve siyah çürük bölgeler. Meyvelerde mumyalaşma görülebilir. Mantar enfeksiyonları ve güneş yanığı kaynaklıdır.",
        "organik_tedavi": "Etkilenen kısımları budayarak uzaklaştırın ve imha edin. Bakır bazlı organik fungisitler uygulayın. Budama aletlerini dezenfekte edin.",
        "kimyasal_tedavi": "Mancozeb veya kaptan içerikli fungisitleri düzenli aralıklarla uygulayın.",
        "onleme": "Kışlayan hastalık kaynaklarını (mumyalaşmış meyve, ölü dal) temizleyin. Hava sirkülasyonu için budama yapın.",
    },
    "Common_rust": {
        "hastalik_tr": "Yaygın Pas",
        "belirtiler": "Yaprakların her iki yüzünde turuncu-kahverengi, toz halinde spor keseleri (pas). İlerledikçe yapraklar sararıp kurur. Puccinia sorghi mantarı kaynaklıdır.",
        "organik_tedavi": "Erken evrede etkilenen yaprakları temizleyin. Kükürt bazlı organik fungisitler uygulanabilir.",
        "kimyasal_tedavi": "Mancozeb veya triazol grubu fungisitleri belirtiler görülür görülmez uygulayın.",
        "onleme": "Pasa dayanıklı çeşitler tercih edin. Bitkiler arası mesafeyi açın. Nemli ve serin dönemlerde sık kontrol yapın.",
    },
    "Bacterial_spot": {
        "hastalik_tr": "Bakteriyel Leke",
        "belirtiler": "Yapraklarda küçük, koyu, su emmiş görünümlü lekeler; çevrelerinde sarı hale. Lekeler birleşerek yaprak dökülmesine yol açar. Xanthomonas bakterisi kaynaklıdır.",
        "organik_tedavi": "Bakır bazlı bakterisitler uygulayın. Hastalıklı bitkileri sağlıklılardan izole edin. Sulama sırasında yaprakları ıslatmayın.",
        "kimyasal_tedavi": "Bakır + mancozeb kombinasyonu kullanılabilir. Bakteriyel hastalıklarda antibiyotik bazlı ürünler (etikete göre) tercih edilebilir.",
        "onleme": "Sertifikalı, hastalıksız tohum/fide kullanın. Islak bitkilerle çalışmaktan kaçının. Ekim nöbeti uygulayın.",
    },
    "Septoria_leaf_spot": {
        "hastalik_tr": "Septoria Yaprak Lekesi",
        "belirtiler": "Yapraklarda küçük, yuvarlak, gri merkezli ve koyu kenarlı lekeler; ortasında minik siyah noktalar (sporlar). Alt yapraklardan başlar. Septoria mantarı kaynaklıdır.",
        "organik_tedavi": "Alt yaprakları temizleyin ve imha edin. Bakır bazlı organik fungisitler uygulayın. Malçlama ile toprak sıçramasını azaltın.",
        "kimyasal_tedavi": "Klorotalonil veya mancozeb içerikli fungisitleri 7-14 gün aralıklarla uygulayın.",
        "onleme": "Bitki tabanına sulama yapın (yaprakları ıslatmayın). Ekim nöbeti uygulayın. Enfekteli bitki artıklarını temizleyin.",
    },
    "mosaic_virus": {
        "hastalik_tr": "Mozaik Virüsü",
        "belirtiler": "Yapraklarda sarı-yeşil karışık mozaik desen, buruşma ve şekil bozukluğu. Bitki bodurlaşabilir. Virüs kaynaklıdır ve yaprak biti gibi böceklerle yayılır.",
        "organik_tedavi": "Virüsün tedavisi yoktur; enfekteli bitkileri imha edin. Yayılımı önlemek için yaprak biti gibi taşıyıcı böcekleri neem yağı ile kontrol edin.",
        "kimyasal_tedavi": "Virüse doğrudan etki eden ilaç yoktur. Taşıyıcı böcekler için uygun insektisit kullanın.",
        "onleme": "Dirençli çeşitler kullanın. Aletleri ve elleri dezenfekte edin. Taşıyıcı böceklerle mücadele edin. Enfekteli bitkileri erken uzaklaştırın.",
    },
    "Powdery_mildew": {
        "hastalik_tr": "Külleme (Küllü Mildiyö)",
        "belirtiler": "Yaprak ve sürgün yüzeyinde beyaz-gri, pudramsı mantar tabakası. İlerledikçe yapraklar sararır ve deforme olur. Sıcak-kuru gündüz, serin-nemli gece koşullarında yaygındır.",
        "organik_tedavi": "Kükürt bazlı organik fungisitler veya süt-su karışımı (1:9) uygulanabilir. Etkilenen yaprakları temizleyin. Neem yağı da etkilidir.",
        "kimyasal_tedavi": "Kükürt, miklobutanil veya triazol grubu fungisitleri uygulayın.",
        "onleme": "Hava sirkülasyonunu artırın (budama, aralık). Gölgeli ve nemli ortamlardan kaçının. Dirençli çeşitler tercih edin.",
    },
    "Apple_scab": {
        "hastalik_tr": "Elma Karalekesi",
        "belirtiler": "Yaprak ve meyvelerde zeytin yeşili-kahverengi, kadifemsi lekeler. İlerledikçe yapraklar sararıp dökülür. Venturia inaequalis mantarı, nemli ilkbahar koşullarında yaygındır.",
        "organik_tedavi": "Yere düşen enfekteli yaprakları toplayıp uzaklaştırın (kışlama kaynağını yok eder). Kükürt veya bakır bazlı organik fungisitler kullanın.",
        "kimyasal_tedavi": "Tomurcuklanma döneminden itibaren kaptan veya miklobutanil içerikli fungisitleri koruyucu olarak uygulayın.",
        "onleme": "Dayanıklı elma çeşitleri tercih edin. Ağaç içini budayarak hava akışını sağlayın. Sonbaharda düşen yaprakları mutlaka temizleyin.",
    },
    "Cedar_apple_rust": {
        "hastalik_tr": "Sedir Elma Pası",
        "belirtiler": "Yaprakların üst yüzeyinde parlak sarı-turuncu lekeler, alt yüzeyde tüysü çıkıntılar. Gymnosporangium mantarı kaynaklıdır ve yaşam döngüsü için ardıç/sedir ağaçlarına ihtiyaç duyar.",
        "organik_tedavi": "Yakındaki ardıç/sedir ağaçlarındaki mantar keselerini (gal) temizleyin. Kükürt bazlı organik fungisitler uygulanabilir.",
        "kimyasal_tedavi": "İlkbaharda miklobutanil veya mancozeb içerikli fungisitleri koruyucu olarak uygulayın.",
        "onleme": "Elma bahçesini ardıç/sedir ağaçlarından uzak tutun. Dayanıklı çeşitler seçin.",
    },
    "Cercospora": {
        "hastalik_tr": "Cercospora Yaprak Lekesi",
        "belirtiler": "Yapraklarda gri merkezli, koyu kahverengi-morumsu kenarlı yuvarlak lekeler. İlerledikçe yapraklar sararıp kurur. Cercospora mantarı kaynaklıdır.",
        "organik_tedavi": "Etkilenen yaprakları uzaklaştırın ve imha edin. Bakır bazlı organik fungisitler uygulayın.",
        "kimyasal_tedavi": "Mancozeb veya triazol grubu fungisitleri düzenli aralıklarla uygulayın.",
        "onleme": "Ekim nöbeti uygulayın. Hava sirkülasyonu için sık ekimden kaçının. Bitki artıklarını temizleyin.",
    },
    "Northern_Leaf_Blight": {
        "hastalik_tr": "Kuzey Yaprak Yanıklığı",
        "belirtiler": "Yapraklarda uzun, eliptik (puro biçimli), grimsi-yeşil lekeler; sonradan kahverengiye döner. Mısırda yaygındır. Exserohilum turcicum mantarı kaynaklıdır.",
        "organik_tedavi": "Enfekteli bitki artıklarını temizleyin ve toprağa gömün. Erken evrede etkilenen yaprakları uzaklaştırın.",
        "kimyasal_tedavi": "Gerekirse mancozeb veya triazol grubu fungisitleri uygulayın.",
        "onleme": "Dayanıklı çeşitler kullanın. Ekim nöbeti (rotasyon) uygulayın. Hasat sonrası tarla artıklarını temizleyin.",
    },
    "Esca": {
        "hastalik_tr": "Esca Hastalığı",
        "belirtiler": "Üzüm asmasında yapraklar arası 'kaplan çizgisi' deseni (damarlar arası sararma/kızarma). Odun dokusunda çürüme. Birden fazla mantarın neden olduğu kronik bir hastalıktır.",
        "organik_tedavi": "Etkilenen dalları budayarak uzaklaştırın. Budama yaralarını macun/koruyucu ile kapatın. Aletleri dezenfekte edin.",
        "kimyasal_tedavi": "Doğrudan etkili kimyasal tedavi sınırlıdır; budama yaralarının korunması esastır.",
        "onleme": "Budamayı kuru havada yapın ve yaraları koruyun. Sağlıklı fidan kullanın. Aşırı stresten (su/besin) kaçının.",
    },
    "Leaf_blight": {
        "hastalik_tr": "Yaprak Yanıklığı",
        "belirtiler": "Yapraklarda düzensiz, kahverengi kuru lekeler ve yanıklık görünümü. Çeşitli mantarlar kaynaklıdır. İlerledikçe yaprak dökülmesine yol açar.",
        "organik_tedavi": "Etkilenen yaprakları temizleyin ve imha edin. Bakır bazlı organik fungisitler uygulayın.",
        "kimyasal_tedavi": "Mancozeb veya klorotalonil içerikli fungisitleri düzenli aralıklarla uygulayın.",
        "onleme": "Hava sirkülasyonunu artırın. Yaprakları ıslatmayan sulama yapın. Bitki artıklarını temizleyin.",
    },
    "Haunglongbing": {
        "hastalik_tr": "Turunçgil Yeşillenmesi (Huanglongbing)",
        "belirtiler": "Yapraklarda asimetrik, damarlar boyunca düzensiz sararma (benekli sararma). Meyveler küçük, çarpık ve acı kalır. Bakteriyel bir hastalıktır ve psyllid (turunçgil psillidi) böceğiyle yayılır. Tedavisi yoktur.",
        "organik_tedavi": "Kesin tedavisi yoktur. Enfekteli ağaçları uzaklaştırın. Taşıyıcı psyllid böceğini neem yağı gibi organik yöntemlerle kontrol edin.",
        "kimyasal_tedavi": "Hastalığa doğrudan etkili ilaç yoktur. Taşıyıcı böcek için uygun insektisit kullanılır.",
        "onleme": "Sertifikalı, hastalıksız fidan kullanın. Psyllid böceğiyle etkin mücadele edin. Enfekteli ağaçları erken tespit edip uzaklaştırın.",
    },
    "Leaf_Mold": {
        "hastalik_tr": "Yaprak Küfü",
        "belirtiler": "Yaprak üst yüzeyinde soluk sarı lekeler, alt yüzeyde zeytin yeşili-kahverengi kadifemsi küf. Özellikle serada, yüksek nemde yaygındır. Passalora fulva mantarı kaynaklıdır.",
        "organik_tedavi": "Havalandırmayı artırın ve nemi düşürün. Etkilenen yaprakları temizleyin. Bakır bazlı organik fungisitler uygulanabilir.",
        "kimyasal_tedavi": "Klorotalonil veya mancozeb içerikli fungisitleri uygulayın.",
        "onleme": "Serada nem oranını düşürün ve havalandırın. Bitkiler arası mesafeyi açın. Sulamayı sabah yapın.",
    },
    "Spider_mites": {
        "hastalik_tr": "Kırmızı Örümcek (Akar)",
        "belirtiler": "Yapraklarda küçük sarı-beyaz noktacıklar (beslenme izleri), ilerledikçe bronzlaşma. Yaprak altında ince ağ örgüsü. Sıcak ve kuru koşullarda hızla çoğalır. Bir zararlı akardır.",
        "organik_tedavi": "Yaprakları su ile yıkayın. Neem yağı veya insektisidal sabun uygulayın. Doğal düşmanları (avcı akarlar) destekleyin.",
        "kimyasal_tedavi": "Akarisit (akara özel ilaç) uygulayın. Aynı etken maddeyi tekrar tekrar kullanmayın (direnç gelişir).",
        "onleme": "Nem seviyesini artırın (akarlar kuru sever). Bitkileri düzenli kontrol edin. Toz birikimini önleyin.",
    },
    "Target_Spot": {
        "hastalik_tr": "Hedef Leke",
        "belirtiler": "Yapraklarda iç içe halkalı (hedef tahtası benzeri) kahverengi lekeler. Meyve ve saplarda da görülebilir. Corynespora cassiicola mantarı kaynaklıdır.",
        "organik_tedavi": "Etkilenen yaprakları temizleyin. Bakır bazlı organik fungisitler uygulayın. Bitkiler arası mesafeyi açın.",
        "kimyasal_tedavi": "Klorotalonil veya mancozeb içerikli fungisitleri düzenli aralıklarla uygulayın.",
        "onleme": "Hava sirkülasyonunu artırın. Yaprakları ıslatmayan sulama yapın. Ekim nöbeti uygulayın.",
    },
    "Yellow_Leaf_Curl_Virus": {
        "hastalik_tr": "Sarı Yaprak Kıvırcıklık Virüsü",
        "belirtiler": "Yapraklarda yukarı doğru kıvrılma, sararma ve küçülme. Bitki bodurlaşır, verim düşer. Virüs kaynaklıdır ve beyaz sinek (Bemisia) ile yayılır.",
        "organik_tedavi": "Virüsün tedavisi yoktur; enfekteli bitkileri imha edin. Beyaz sineği sarı yapışkan tuzaklar ve neem yağı ile kontrol edin.",
        "kimyasal_tedavi": "Virüse doğrudan etkili ilaç yoktur. Taşıyıcı beyaz sinek için uygun insektisit kullanın.",
        "onleme": "Dirençli çeşitler kullanın. Beyaz sinekle etkin mücadele edin. Fideleri örtü/ağ ile koruyun. Enfekteli bitkileri erken uzaklaştırın.",
    },
}
