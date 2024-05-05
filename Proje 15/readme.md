# Çevrimiçi Kitap Okuma ve Paylaşım Platformu Kılavuzu

Bu kılavuz, Çevrimiçi Kitap Okuma ve Paylaşım Platformu adlı uygulamanın nasıl kullanılacağını anlatmaktadır. Ayrıca, uygulamanın çalışma mantığını ve yapılandırılmasını açıklayan teknik bilgiler de içermektedir.

## Kullanım Kılavuzu

### 1. Giriş Yapma

Uygulamayı kullanabilmek için ilk olarak giriş yapmanız gerekmektedir. Giriş ekranında kullanıcı adınızı ve şifrenizi girerek "Giriş Yap" düğmesine tıklayınız. Eğer kullanıcı adı ve şifre doğru ise ana sayfaya yönlendirileceksiniz.

### 2. Kitapları Listeleme

Ana sayfada tüm kitapların bir listesi görüntülenir. Bu listeden istediğiniz bir kitaba tıklayarak kitap hakkında detaylı bilgileri görebilirsiniz.

### 3. Kitap Detayları

Seçtiğiniz bir kitabın detayları sayfasında kitabın yazarı, yayınevi ve kısa bir hikayesi görüntülenir. Ayrıca kitaba yapılan yorumları görebilir ve yeni yorum ekleyebilirsiniz.

### 4. Kitap İçeriği

Kitap detayları sayfasında "Kitap İçeriğini Göster" düğmesine tıklayarak seçtiğiniz kitabı okuyabilirsiniz. Kitabın içeriği, metin formatında görüntülenir.

### 5. Kitabı Paylaşma

Kitap detayları sayfasında "Kitabı Paylaş" düğmesine tıklayarak seçtiğiniz kitabı paylaşabilirsiniz. Bu şekilde diğer kullanıcılar da sizin paylaştığınız kitapları görebilir.

### 6. Çıkış Yapma

Kullanımınızı tamamladıktan sonra uygulamadan çıkış yapmak için sağ üst köşedeki çıkış düğmesine tıklayabilirsiniz.

## Teknik Bilgi ve Yapılandırma

### PyQt5 Kullanımı

Uygulama, PyQt5 kütüphanesini kullanarak Python dilinde geliştirilmiştir. Arayüz tasarımı ve etkileşimleri bu kütüphane üzerinden gerçekleştirilmiştir.

### Veri Yapıları

Uygulama içerisinde kullanılan temel veri yapıları şunlardır:

- Kitap sınıfı: Kitapların özelliklerini ve metodlarını tanımlar.
- User sınıfı: Kullanıcıların özelliklerini ve kullanıcı işlemlerini tanımlar.
- Comment sınıfı: Yorumların özelliklerini ve yorum işlemlerini tanımlar.

### Uygulama Akışı

1. Kullanıcı giriş yaptıktan sonra ana sayfaya yönlendirilir.
2. Ana sayfada kitap listesi gösterilir.
3. Kullanıcı bir kitaba tıkladığında kitap detayları sayfasına yönlendirilir.
4. Kitap detayları sayfasında kitap bilgileri ve yorumlar görüntülenir.
5. Kullanıcı kitap içeriğini okuyabilir veya paylaşabilir.
6. Çıkış yapmak istediğinde çıkış düğmesine tıklayarak uygulamadan çıkabilir.

Bu kılavuz ve teknik belge, Çevrimiçi Kitap Okuma ve Paylaşım Platformu uygulamasını kullanırken ve anlamaya çalışırken size rehberlik etmek için tasarlanmıştır. İyi okumalar ve paylaşımlar dileriz!
