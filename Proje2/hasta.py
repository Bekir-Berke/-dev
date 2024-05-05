class Hasta:
    def __init__(self, ad, soyad, tc_no, yas, cinsiyet, randevu_geçmişi):
        self.ad = ad
        self.soyad = soyad
        self.tc_no = tc_no
        self.yas = yas
        self.cinsiyet = cinsiyet
        self.randevu_gecmisi = randevu_geçmişi

    def randevu_al(self, randevu):
        self.randevu_gecmisi.append(randevu)

    def randevu_iptal(self, randevu):
        self.randevu_gecmisi.remove(randevu)