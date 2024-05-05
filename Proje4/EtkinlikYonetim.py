import Bilet
class EtkinlikYonetimSistemi:
    def __init__(self):
        self.etkinlikler = []
        self.katilimcilar = []
        self.biletler = []

    def etkinlik_ekle(self, etkinlik):
        self.etkinlikler.append(etkinlik)

    def katilimci_ekle(self, katilimci):
        self.katilimcilar.append(katilimci)

    def bilet_sat(self, etkinlik, katilimci, bilet_turu):
        yeni_bilet = Bilet.Bilet(etkinlik, katilimci, bilet_turu)
        self.biletler.append(yeni_bilet)
