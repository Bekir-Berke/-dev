class Kitap:
    def __init__(self, kitap_id, ad, yazar):
        self.kitap_id = kitap_id
        self.ad = ad
        self.yazar = yazar
        self.durum = "Rafta"

    def durum_guncelle(self, durum):
        self.durum = durum