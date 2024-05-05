class Musteri:
    def __init__(self, ad, soyad, telefon, sifre):
        self.ad = ad
        self.soyad = soyad
        self.telefon = telefon
        self.sifre = sifre

    def __str__(self):
        return f"{self.ad} {self.soyad} {self.telefon}"