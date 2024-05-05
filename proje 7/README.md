## Kullanıcı Kılavuzu: Spor Takip Uygulaması

### Giriş
Spor Takip Uygulaması, sporcuların bilgilerini ve antrenman programlarını yönetmek için tasarlanmış bir yazılımdır. Bu uygulama ile sporcuları kaydedebilir, her birine özel antrenman programları oluşturabilir ve tüm antrenmanları listeleyebilirsiniz.

### Başlangıç
Uygulamayı başlatmak için uygulama ikonuna çift tıklayın. Ana ekran karşınıza çıkacaktır.

### Sporcu Ekleme
1. **Sporcu Adını Girin:** Ana ekranda, 'Sporcu Adını Girin' metin kutusuna sporcu adını yazın.
2. **Spor Dalı Seçin:** Açılır menüden sporcu için uygun olan spor dalını seçin. Mevcut spor dalları Futbol, Basketbol, Yüzme, Tenis ve Atletizm'dir.
3. **Sporcu Ekle Butonu:** Bilgileri doldurduktan sonra 'Sporcu Ekle' butonuna tıklayarak sporcu listesine ekleyin.

### Antrenman Programı Ekleme
1. **Sporcu Seçimi:** Sporcular listesinden bir sporcu seçin. Bu sporcu için antrenman programı oluşturacaksınız.
2. **Antrenman Adını Girin:** 'Antrenman Adını Girin' metin kutusuna antrenmanın adını yazın.
3. **Antrenman Detaylarını Girin:** 'Antrenman Detaylarını Girin' metin kutusuna antrenmanın ayrıntılarını yazın.
4. **Periyot Seçimi:** Antrenmanın tekrarlanma sıklığını belirlemek için 'Periyot' açılır menüsünden bir seçim yapın. Günlük, Haftalık veya Aylık seçenekleri mevcuttur.
5. **Antrenman Ekle Butonu:** Gerekli bilgileri doldurduktan sonra 'Antrenman Ekle' butonuna basarak antrenmanı sporcunun programına ekleyin.

### Antrenman Listesi Görüntüleme
1. **Antrenmanları Göster Butonu:** Ana ekrandaki 'Antrenmanları Göster' butonuna tıklayarak tüm sporcuların antrenman programlarını içeren bir liste açılır.
2. Liste, her bir sporcu için oluşturulan antrenmanları sporcu adı, antrenman adı, detaylar ve periyot şeklinde gösterir.

### Veri Kaydetme ve Yükleme
- Uygulama, sporcu ve antrenman bilgilerini otomatik olarak `sporcular_data.pkl` dosyasına kaydeder.
- Uygulama başlatıldığında, bu dosya varsa mevcut veriler otomatik olarak yüklenir. Eğer dosya yoksa, yeni bir veri dosyası oluşturulur.

### Çıkış Yapma
- Uygulamadan çıkmak için ana pencerenin sağ üst köşesindeki kapatma (X) butonuna tıklayın.

### Sorun Giderme
- Eğer veri yükleme veya kaydetme sırasında bir hata ile karşılaşırsanız, veri dosyasının doğru yolda olduğundan ve yazılabilir olduğundan emin olun.
- Sporcu veya antrenman bilgileri eksik girildiğinde sistem uygun hata mesajları verecektir. Gerekli alanları doğru ve eksiksiz doldurduğunuzdan emin olun.