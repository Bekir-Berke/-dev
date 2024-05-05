class Odunc:
    def __init__(self, kitap, uye):
        self.kitap = kitap
        self.uye = uye

    def odunc_al(self):
        self.kitap.durum_guncelle("Ödünç alındı")

    def iade_et(self):
        self.kitap.durum_guncelle("Rafta")

    def odunc_bilgisi(self):
        return f"{self.uye.ad} {self.uye.soyad}'a ait {self.kitap.ad} kitabı {self.kitap.durum} durumunda."