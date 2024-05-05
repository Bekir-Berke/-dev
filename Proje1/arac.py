class Arac:
    def __init__(self, id, marka, model, vites, yakit, yil, kiralama, fiyat):
        self.id = id
        self.marka = marka
        self.model = model
        self.yil = yil
        self.vites = vites
        self.yakit = yakit
        self.kiralama = kiralama
        self.fiyat = fiyat
    def durum_güncelle(self, durum):
        self.kiralama = durum
