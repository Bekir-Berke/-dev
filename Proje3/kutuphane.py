import Odunc
class Kutuphane:
    def __init__(self):
        self.kitaplar = []
        self.uyeler = []
        self.odunc_islemleri = []

    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)

    def uye_ekle(self, uye):
        self.uyeler.append(uye)

    def odunc_al(self, kitap_id, uye_id):
        kitap = next((k for k in self.kitaplar if k.kitap_id == kitap_id), None)
        uye = next((u for u in self.uyeler if u.uye_id == uye_id), None)
        if kitap and uye:
            if kitap.durum == "Rafta":
                odunc = Odunc.Odunc(kitap, uye)
                odunc.odunc_al()
                self.odunc_islemleri.append(odunc)
                return f"{kitap.ad} kitabı {uye.ad} {uye.soyad}'a ödünç verildi."
            else:
                return "Bu kitap zaten ödünç alınmış."
        else:
            return "Kitap veya üye bulunamadı."

    def iade_et(self, kitap_id):
        odunc = next((o for o in self.odunc_islemleri if o.kitap.kitap_id == kitap_id), None)
        if odunc:
            odunc.iade_et()
            self.odunc_islemleri.remove(odunc)
            return f"{odunc.kitap.ad} kitabı iade edildi."
        else:
            return "Bu kitap ödünç alınmamış."

    def odunc_bilgisi(self):
        if self.odunc_islemleri:
            for odunc in self.odunc_islemleri:
                print(odunc.odunc_bilgisi())
        else:
            print("Şu anda ödünç kitap yok.")