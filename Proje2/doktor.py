class Doktor:
    def __init__(self, isim, uzmanlik_alani, musaitlik_durumu="Müsait"):
        self.isim = isim
        self.uzmanlik_alani = uzmanlik_alani
        self.musaitlik_durumu = musaitlik_durumu

    def musaitlik_degistir(self, durum):
        self.musaitlik_durumu = durum