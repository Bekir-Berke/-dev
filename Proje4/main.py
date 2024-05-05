import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Etkinlik:
    def __init__(self, etkinlik_adi, tarih, yer):
        self.etkinlik_adi = etkinlik_adi
        self.tarih = tarih
        self.yer = yer

class Katilimci:
    def __init__(self, ad, soyad, email):
        self.ad = ad
        self.soyad = soyad
        self.email = email

class Bilet:
    def __init__(self, etkinlik, katilimci, bilet_turu):
        self.etkinlik = etkinlik
        self.katilimci = katilimci
        self.bilet_turu = bilet_turu

class EtkinlikYonetimSistemi:
    def __init__(self):
        self.etkinlikler = []
        self.katilimcilar = []
        self.biletler = []
        self.biletTuru = [{"tur":"Gold", "fiyat":100}, {"tur":"Silver", "fiyat":50}, {"tur":"Standard", "fiyat":25}]
    def etkinlik_ekle(self, etkinlik):
        self.etkinlikler.append(etkinlik)

    def katilimci_ekle(self, katilimci):
        self.katilimcilar.append(katilimci)

    def bilet_sat(self, etkinlik, katilimci, bilet_turu):
        yeni_bilet = Bilet(etkinlik, katilimci, bilet_turu)
        self.biletler.append(yeni_bilet)

class EtkinlikYonetimSistemiGUI:
    def __init__(self, root):
        self.ana_pencere = root
        self.ana_pencere.title("Etkinlik Yönetim Sistemi")
        self.etkinlik_yonetim_sistemi = EtkinlikYonetimSistemi()
        self.etkinlik_ekleme_formu()
        self.katilimci_ekleme_formu()
        self.bilet_satis_formu()

    def etkinlik_ekleme_formu(self):
        etkinlik_ekleme_frame = ttk.LabelFrame(self.ana_pencere, text="Etkinlik Ekle")
        etkinlik_ekleme_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        ttk.Label(etkinlik_ekleme_frame, text="Etkinlik Adı:").grid(row=0, column=0, padx=10, pady=10)
        self.etkinlik_adi = ttk.Entry(etkinlik_ekleme_frame)
        self.etkinlik_adi.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(etkinlik_ekleme_frame, text="Tarih:").grid(row=1, column=0, padx=10, pady=10)
        self.tarih = ttk.Entry(etkinlik_ekleme_frame)
        self.tarih.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(etkinlik_ekleme_frame, text="Yer:").grid(row=2, column=0, padx=10, pady=10)
        self.yer = ttk.Entry(etkinlik_ekleme_frame)
        self.yer.grid(row=2, column=1, padx=10, pady=10)

        ttk.Button(etkinlik_ekleme_frame, text="Etkinlik Ekle", command=self.etkinlik_ekle).grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    def etkinlik_ekle(self):
        etkinlik_adi = self.etkinlik_adi.get()
        tarih = self.tarih.get()
        yer = self.yer.get()
        etkinlik = Etkinlik(etkinlik_adi, tarih, yer)
        self.etkinlik_yonetim_sistemi.etkinlik_ekle(etkinlik)
        self.etkinlik_adi.delete(0, "end")
        self.tarih.delete(0, "end")
        self.yer.delete(0, "end")
        messagebox.showinfo("Etkinlik Ekleme", "Etkinlik eklendi.")
        self.guncelle_combobox()

    def katilimci_ekleme_formu(self):
        katilimci_ekleme_frame = ttk.LabelFrame(self.ana_pencere, text="Katılımcı Ekle")
        katilimci_ekleme_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        ttk.Label(katilimci_ekleme_frame, text="Ad:").grid(row=0, column=0, padx=10, pady=10)
        self.ad = ttk.Entry(katilimci_ekleme_frame)
        self.ad.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(katilimci_ekleme_frame, text="Soyad:").grid(row=1, column=0, padx=10, pady=10)
        self.soyad = ttk.Entry(katilimci_ekleme_frame)
        self.soyad.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(katilimci_ekleme_frame, text="Email:").grid(row=2, column=0, padx=10, pady=10)
        self.email = ttk.Entry(katilimci_ekleme_frame)
        self.email.grid(row=2, column=1, padx=10, pady=10)

        ttk.Button(katilimci_ekleme_frame, text="Katılımcı Ekle", command=self.katilimci_ekle).grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    def katilimci_ekle(self):
        ad = self.ad.get()
        soyad = self.soyad.get()
        email = self.email.get()
        katilimci = Katilimci(ad, soyad, email)
        self.etkinlik_yonetim_sistemi.katilimci_ekle(katilimci)
        self.ad.delete(0, "end")
        self.soyad.delete(0, "end")
        self.email.delete(0, "end")
        messagebox.showinfo("Katılımcı Ekleme", "Katılımcı eklendi.")
        self.guncelle_combobox()

    def bilet_satis_formu(self):
        bilet_satis_frame = ttk.LabelFrame(self.ana_pencere, text="Bilet Satış")
        bilet_satis_frame.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        ttk.Label(bilet_satis_frame, text="Etkinlik:").grid(row=0, column=0, padx=10, pady=10)
        self.etkinlik = ttk.Combobox(bilet_satis_frame)
        self.etkinlik.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(bilet_satis_frame, text="Katılımcı:").grid(row=1, column=0, padx=10, pady=10)
        self.katilimci = ttk.Combobox(bilet_satis_frame)
        self.katilimci.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(bilet_satis_frame, text="Bilet Türü:").grid(row=2, column=0, padx=10, pady=10)
        self.bilet_turu = ttk.Combobox(bilet_satis_frame)
        self.bilet_turu.grid(row=2, column=1, padx=10, pady=10)
        self.bilet_turu.bind("<<ComboboxSelected>>", self.guncelle_fiyat)

        ttk.Label(bilet_satis_frame, text="Fiyat:").grid(row=3, column=0, padx=10, pady=10)
        self.fiyatlar = ttk.Label(bilet_satis_frame, text = "")
        self.fiyatlar.grid(row=3, column=1, padx=10, pady=10)

        ttk.Button(bilet_satis_frame, text="Bilet Sat", command=self.bilet_sat).grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        self.guncelle_combobox()

    def guncelle_combobox(self):
        self.etkinlik["values"] = [etkinlik.etkinlik_adi for etkinlik in self.etkinlik_yonetim_sistemi.etkinlikler]
        self.katilimci["values"] = [katilimci.ad for katilimci in self.etkinlik_yonetim_sistemi.katilimcilar]
        self.bilet_turu["values"] = [bilet["tur"] for bilet in self.etkinlik_yonetim_sistemi.biletTuru]

    def guncelle_fiyat(self, event):
        secilen_tur = self.bilet_turu.get()
        for bilet in self.etkinlik_yonetim_sistemi.biletTuru:
            if bilet["tur"] == secilen_tur:
                self.fiyatlar.config(text=f"{bilet['fiyat']} ₺")

    def bilet_sat(self):
        etkinlik = [etkinlik for etkinlik in self.etkinlik_yonetim_sistemi.etkinlikler if etkinlik.etkinlik_adi == self.etkinlik.get()][0]
        katilimci = [katilimci for katilimci in self.etkinlik_yonetim_sistemi.katilimcilar if katilimci.ad == self.katilimci.get()][0]
        bilet_turu = self.bilet_turu.get()
        self.etkinlik_yonetim_sistemi.bilet_sat(etkinlik, katilimci, bilet_turu)
        self.etkinlik.set('')
        self.katilimci.set('')
        self.bilet_turu.set('')
        messagebox.showinfo("Bilet Satış", "Bilet satıldı.")

if __name__ == "__main__":
    root = tk.Tk()
    etkinlik_yonetim_sistemi_gui = EtkinlikYonetimSistemiGUI(root)
    root.mainloop()
