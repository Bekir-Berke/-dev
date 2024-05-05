## Kullanıcı Kılavuzu: Stok Takip Sistemi

### Giriş
Stok Takip Sistemi, ürün envanterinizi yönetmenizi ve stoklarınızı güncel tutmanızı sağlayan bir yazılımdır. Ürünleri sisteme ekleyebilir, stok miktarlarını ve fiyatlarını güncelleyebilir ve tüm değişiklikleri kaydedebilirsiniz.

### Sisteme Giriş Yapma
1. Uygulamayı başlattığınızda, bir kullanıcı adı ve şifre ile giriş yapmanız istenecektir.
2. Varsayılan kullanıcı adı ve şifre şunlardır:
   - Kullanıcı Adı: `admin`
   - Şifre: `admin`
3. Doğru bilgileri girdiğinizde, ana arayüze yönlendirileceksiniz.

### Ana Arayüz
Ana arayüz, ürünleri ekleyebileceğiniz, mevcut stokları görebileceğiniz ve değişiklikleri kaydedebileceğiniz bölümleri içerir.

#### Ürün Ekleme
1. "Ürün Adı Giriniz" alanına ürünün adını yazın.
2. "Stok Miktarı Giriniz" alanına ürünün stok miktarını girin. Bu alan yalnızca sayısal değerler kabul eder.
3. "Ürün Fiyatı Giriniz" alanına ürünün fiyatını girin. Bu alan ondalıklı sayıları da kabul eder.
4. "Ürün Ekle" düğmesine basarak ürünü sisteme ekleyin. Ekleme işlemi başarılı olduğunda, ürün otomatik olarak stok tablosunda görünecektir.

#### Stok ve Fiyatları Düzenleme
1. "Stok Düzenle" düğmesine tıklayarak stok düzenleme diyalog penceresini açın.
2. Açılan pencerede, istediğiniz ürünün yeni stok miktarını ve fiyatını güncelleyebilirsiniz.
3. Her bir değişikliği, ilgili satırdaki "Yeni Stok Miktarı" ve "Yeni Fiyat" alanlarına girin.
4. "Stokları ve Fiyatları Güncelle" düğmesine basarak tüm değişiklikleri onaylayın.

#### Stokları Kaydetme
1. Tüm değişiklikler yapıldıktan sonra, "Stokları Kaydet" düğmesine basarak tüm bilgileri JSON formatında bir dosyaya kaydedin.
2. Bu işlem, yapmış olduğunuz tüm değişikliklerin kalıcı hale gelmesini sağlar.

### Sistemden Çıkış Yapma
1. Uygulama penceresinin sağ üst köşesinde bulunan "X" simgesine tıklayarak programdan çıkış yapabilirsiniz.

### Sorun Giderme
- Eğer giriş bilgileriniz çalışmıyorsa, kullanıcı adı ve şifreyi doğru girdiğinizden emin olun.
- Stok veya fiyat bilgilerini girerken hatalı veri tipi kullanıyorsanız, sistemin sağladığı hata mesajlarını dikkate alın.