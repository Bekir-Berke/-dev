import tkinter as tk
from tkinter import ttk, messagebox

class Urun:
    def __init__(self, ad, fiyat, stok):
        self.ad = ad
        self.fiyat = fiyat
        self.stok = stok  

    def stok_guncelle(self, miktar):
        self.stok += miktar

class Siparis:
    def __init__(self, siparis_numarasi, icerik, musteri_bilgileri):
        self.siparis_numarasi = siparis_numarasi
        self.icerik = icerik  
        self.musteri_bilgileri = musteri_bilgileri

    def siparis_fiyati(self):
        toplam_fiyat = sum(sum(urun.fiyat) if isinstance(urun.fiyat, list) 
                           else urun.fiyat for urun in self.icerik)
        return toplam_fiyat

class Musteri:
    def __init__(self, ad, adres):
        self.ad = ad
        self.adres = adres
        self.siparis_gecmisi = []  

    def siparis_gecmisine_ekle(self, siparis):
        self.siparis_gecmisi.append(siparis)

class Restoran:
    def __init__(self):
        self.menu = [
            Urun("Konser", 600.00, 10),
            Urun("Spor Etkinliği", 1150.00, 20),
            Urun("Festival", 450.00, 15),
            Urun("Seminer", 30.00, 25),
            Urun("Tiyatro", 50.00, 10),
            Urun("Sinema", 200.00, 30)
        ]
        self.musteriler = []

    def menuyu_goruntule(self):
        return self.menu

class GirisEkrani:
    def __init__(self, ana_pencere):
        self.ana_pencere = ana_pencere
        self.ana_pencere.title("Müşteri Girişi")

        self.ana_pencere.configure(bg="#f0f0f0")

        self.etiket = tk.Label(ana_pencere, text="Adınızı ve Telefon Numarınızı Giriniz", bg="#f0f0f0", font=("Helvetica", 18))
        self.etiket.pack(pady=20)

        self.ad_etiket = tk.Label(ana_pencere, text="Adınız:", bg="#f0f0f0", font=("Helvetica", 12))
        self.ad_etiket.pack()
        self.ad_giris = tk.Entry(ana_pencere)
        self.ad_giris.pack()

        self.adres_etiket = tk.Label(ana_pencere, text="Telefon:", bg="#f0f0f0", font=("Helvetica", 12))
        self.adres_etiket.pack()
        self.adres_giris = tk.Entry(ana_pencere)
        self.adres_giris.pack()

        self.devam_butonu = tk.Button(ana_pencere, text="Devam Et", command=self.devam_et, bg="#0c8081", fg="white", font=("Helvetica", 12))
        self.devam_butonu.pack(pady=10, padx=20, ipadx=10, ipady=5)

    def devam_et(self):
        ad = self.ad_giris.get()
        adres = self.adres_giris.get()
        if ad and adres:
            self.ana_pencere.destroy()
            uygulama = RestoranUygulamasi(tk.Tk(), ad, adres)
        else:
            messagebox.showerror("Hata", "Lütfen adınızı ve adresinizi girin.")

class RestoranUygulamasi:
    def __init__(self, ana_pencere, ad, adres):
        self.ana_pencere = ana_pencere
        self.ana_pencere.title("Etkinlik ve Bilet Satış Platformu")

        self.ana_pencere.configure(bg="#f0f0f0")

        self.etiket = tk.Label(ana_pencere, text="Etkinlik ve Bilet Satış Platformu ", bg="#f0f0f0", font=("Helvetica", 18))
        self.etiket.pack(pady=20)

        self.menu_butonu = tk.Button(ana_pencere, text="Etkinlikleri Görüntüle", command=self.menuyu_goruntule, bg="#0c8081", fg="white", font=("Helvetica", 12))
        self.menu_butonu.pack(pady=10, padx=20, ipadx=10, ipady=5)

        self.siparis_butonu = tk.Button(ana_pencere, text="Bilet Al", command=self.siparis_ver, bg="#0c8081", fg="white", font=("Helvetica", 12))
        self.siparis_butonu.pack(pady=10, padx=20, ipadx=10, ipady=5)

        self.siparisler_butonu = tk.Button(ana_pencere, text="Biletlerim", command=self.siparisleri_goruntule, bg="#0c8081", fg="white", font=("Helvetica", 12))
        self.siparisler_butonu.pack(pady=10, padx=20, ipadx=10, ipady=5)

        self.yonetici_butonu = tk.Button(ana_pencere, text="Yönetici", command=self.yonetici_giris, bg="#0c8081", fg="white", font=("Helvetica", 12))
        self.yonetici_butonu.pack(pady=10, padx=20, ipadx=10, ipady=5)

        self.restoran = Restoran()
        self.siparis = None  

        musteri = Musteri(ad=ad, adres=adres)
        musteri_siparis = Siparis(siparis_numarasi=1, icerik=self.restoran.menu[0:2], musteri_bilgileri=musteri)
        musteri.siparis_gecmisine_ekle(musteri_siparis)
        self.restoran.musteriler.append(musteri)

    def menuyu_goruntule(self):
        menu = self.restoran.menuyu_goruntule()
        menu_penceresi = tk.Toplevel(self.ana_pencere)
        menu_penceresi.title("Etkinlikler")
        menu_penceresi.configure(bg="#f0f0f0")  
        for urun in menu:
            etiket = tk.Label(menu_penceresi, text=f"{urun.ad}: {urun.fiyat} TL", bg="#f0f0f0", font=("Helvetica", 12))
            etiket.pack(pady=5, padx=10, anchor="w")

    def siparis_ver(self):
            siparis_penceresi = tk.Toplevel(self.ana_pencere)
            siparis_penceresi.title("Bilet Al")
            siparis_penceresi.configure(bg="#f0f0f0")  
        
            yemekler = [
                "Konser",
                "Spor Etkinliği",
                "Festival",
                "Seminer",
                "Tiyatro",
                "Sinema"
            ]
            icecekler = [
                "Kategori 1",
                "Kategori 2",
                "Kategori 3",
            ]
        
            self.siparis_icerik = []  
        
            yemek_etiket = tk.Label(siparis_penceresi, text="Bilet Seçenekleri:", bg="#f0f0f0", font=("Helvetica", 12))
            yemek_etiket.pack()
        
            self.yemek_secim = tk.StringVar(siparis_penceresi)
            self.yemek_secim.set(yemekler[0])  
        
            yemek_secenekleri = tk.OptionMenu(siparis_penceresi, self.yemek_secim, *yemekler)
            yemek_secenekleri.config(bg="#0c8081", fg="white", font=("Helvetica", 12))
            yemek_secenekleri.pack(pady=5, padx=10, ipadx=5, ipady=3)
        
            icecek_etiket = tk.Label(siparis_penceresi, text="                  Kategori Seçenekleri:               ", bg="#f0f0f0", font=("Helvetica", 12))
            icecek_etiket.pack()
        
            self.icecek_secim = tk.StringVar(siparis_penceresi)
            self.icecek_secim.set(icecekler[0])  
        
            icecek_secenekleri = tk.OptionMenu(siparis_penceresi, self.icecek_secim, *icecekler)
            icecek_secenekleri.config(bg="#0c8081", fg="white", font=("Helvetica", 12))
            icecek_secenekleri.pack(pady=5, padx=10, ipadx=5, ipady=3)
        
            gonder_butonu = tk.Button(siparis_penceresi, text="Satın Al", command=self.siparisi_gonder, bg="#0c8081", fg="white", font=("Helvetica", 12))
            gonder_butonu.pack(pady=10, padx=20, ipadx=10, ipady=5)
        
            self.tutar_etiket = tk.Label(siparis_penceresi, text="", bg="#f0f0f0", font=("Helvetica", 12))
            self.tutar_etiket.pack()

    def siparisi_gonder(self):
        secilen_yemek = self.yemek_secim.get()
        secilen_icecek = self.icecek_secim.get() 

        secilen_yemek_fiyat = [urun.fiyat for urun in self.restoran.menu if urun.ad == secilen_yemek]
        secilen_icecek_fiyat = [urun.fiyat for urun in self.restoran.menu if urun.ad == secilen_icecek]
        

        secilen_yemek_urun = Urun(ad=secilen_yemek, fiyat=secilen_yemek_fiyat, stok=1)
        secilen_icecek_urun = Urun(ad=secilen_icecek, fiyat=secilen_icecek_fiyat, stok=1)

        self.siparis_icerik.append(secilen_yemek_urun) 
        self.siparis_icerik.append(secilen_icecek_urun)

        for urun in self.restoran.menu:
            if urun.ad == secilen_yemek:
                urun.stok -= 1
            elif urun.ad == secilen_icecek:
                urun.stok -= 1

        siparis_tutari = sum(sum(urun.fiyat) for urun in self.siparis_icerik)

        self.tutar_etiket.config(text=f"Bilet Tutarı: {siparis_tutari} TL")

        messagebox.showinfo("Bilet Alındı", "Biletiniz alınmıştır.")

        yeni_siparis = Siparis(siparis_numarasi=len(self.restoran.musteriler[0].siparis_gecmisi) + 1,
                               icerik=self.siparis_icerik,
                               musteri_bilgileri=self.restoran.musteriler[0])

        self.restoran.musteriler[0].siparis_gecmisine_ekle(yeni_siparis)

        self.ana_pencere.deiconify()

    def siparisleri_goruntule(self):
        if not self.restoran.musteriler:
            messagebox.showinfo("Biletlerin", "Henüz bilet satın alınmamış.")
            return

        def sil():
            secili_siparis = treeview.selection()
            if secili_siparis:
                for musteri in self.restoran.musteriler:
                    for siparis in musteri.siparis_gecmisi:
                        if siparis == secili_siparis[0]:
                            musteri.siparis_gecmisi.remove(siparis)
                            break
                treeview.delete(secili_siparis)

        siparisler_penceresi = tk.Toplevel(self.ana_pencere)
        siparisler_penceresi.title("Biletlerim")
        siparisler_penceresi.configure(bg="#f0f0f0")
        
        treeview = ttk.Treeview(siparisler_penceresi, columns=("Müşteri İsmi", "Adres", "Siparişler", "Fiyat"), show="headings")
        treeview.heading("Müşteri İsmi", text="Müşteri İsmi")
        treeview.heading("Adres", text="Telefon")
        treeview.heading("Siparişler", text="Siparişler")
        treeview.heading("Fiyat", text="Fiyat")
        
        for musteri in self.restoran.musteriler:
            for siparis in musteri.siparis_gecmisi:
                siparis_icerik = ', '.join(urun.ad for urun in siparis.icerik)
                siparis_fiyat = siparis.siparis_fiyati()
                treeview.insert("", "end", values=(musteri.ad, musteri.adres, siparis_icerik, siparis_fiyat))
        
        treeview.pack(expand=True, fill="both")

        sil_button = tk.Button(siparisler_penceresi, text="Sil", command=sil, bg="#FF5733", fg="white", font=("Helvetica", 12))
        sil_button.pack(pady=10, padx=20, ipadx=10, ipady=5)

    def yonetici_giris(self):
        yonetici_pencere = tk.Toplevel(self.ana_pencere)
        yonetici_pencere.title("Yönetici Girişi")

        self.kullanici_adi_etiket = tk.Label(yonetici_pencere, text="Kullanıcı Adı:", bg="#f0f0f0", font=("Helvetica", 12))
        self.kullanici_adi_etiket.pack()
        self.kullanici_adi_giris = tk.Entry(yonetici_pencere)
        self.kullanici_adi_giris.pack()

        self.sifre_etiket = tk.Label(yonetici_pencere, text="Şifre:", bg="#f0f0f0", font=("Helvetica", 12))
        self.sifre_etiket.pack()
        self.sifre_giris = tk.Entry(yonetici_pencere, show="*")
        self.sifre_giris.pack()

        giris_butonu = tk.Button(yonetici_pencere, text="Giriş Yap", command=self.yonetici_giris_kontrol, bg="#0c8081", fg="white", font=("Helvetica", 12))
        giris_butonu.pack(pady=10, padx=20, ipadx=10, ipady=5)

    def yonetici_giris_kontrol(self):
        kullanici_adi = self.kullanici_adi_giris.get()
        sifre = self.sifre_giris.get()

        if kullanici_adi == "admin" and sifre == "admin1":
            yonetici_arayuzu = YoneticiArayuzu(self.ana_pencere, self.restoran)
        else:
            messagebox.showerror("Hata", "Yanlış kullanıcı adı veya şifre.")

class YoneticiArayuzu:
    def __init__(self, ana_pencere, restoran):
                self.ana_pencere = ana_pencere
                self.restoran = restoran
        
                self.ana_pencere.withdraw()
        
                self.yonetici_pencere = tk.Toplevel(self.ana_pencere)
                self.yonetici_pencere.title("Yönetici Arayüzü")
        
                self.urun_ekle_butonu = tk.Button(self.yonetici_pencere, text="Etkinlik Ekle", command=self.urun_ekle, bg="#0c8081", fg="white", font=("Helvetica", 12))
                self.urun_ekle_butonu.pack(pady=10, padx=20, ipadx=10, ipady=5)
        
                self.stok_guncelle_butonu = tk.Button(self.yonetici_pencere, text="Bilet Adeti Güncelle", command=self.stok_guncelle, bg="#0c8081", fg="white", font=("Helvetica", 12))
                self.stok_guncelle_butonu.pack(pady=10, padx=20, ipadx=10, ipady=5)
        
                self.fiyat_duzenle_butonu = tk.Button(self.yonetici_pencere, text="Fiyat Düzenle", command=self.fiyat_duzenle, bg="#0c8081", fg="white", font=("Helvetica", 12))
                self.fiyat_duzenle_butonu.pack(pady=10, padx=20, ipadx=10, ipady=5)
        
                self.stok_miktarı_butonu = tk.Button(self.yonetici_pencere, text="Bilet Adeti", command=self.stok_miktarlarini_goster, bg="#0c8081", fg="white", font=("Helvetica", 12))
                self.stok_miktarı_butonu.pack(pady=10, padx=20, ipadx=10, ipady=5)
        
                self.geri_butonu = tk.Button(self.yonetici_pencere, text="Geri", command=self.geri_git, bg="#0c8081", fg="white", font=("Helvetica", 12))
                self.geri_butonu.pack(pady=10, padx=20, ipadx=10, ipady=5)
        
    def stok_miktarlarini_goster(self):
                stok_miktarlari_pencere = tk.Toplevel(self.yonetici_pencere)
                stok_miktarlari_pencere.title("Bilet Adeti")
        
                stok_miktarlari_pencere.configure(bg="#f0f0f0")
        
                for urun in self.restoran.menu:
                    etiket = tk.Label(stok_miktarlari_pencere, text=f"{urun.ad}: {urun.stok} adet", bg="#f0f0f0", font=("Helvetica", 12))
                    etiket.pack(pady=5, padx=10, anchor="w")
        
        
    def geri_git(self):
                self.yonetici_pencere.destroy()
                self.ana_pencere.deiconify()
        

    def urun_ekle(self):
        urun_ekle_pencere = tk.Toplevel(self.yonetici_pencere)
        urun_ekle_pencere.title("Etkinlik Ekle")

        self.urun_adı_etiket = tk.Label(urun_ekle_pencere, text="Etkinlik Adı:", bg="#f0f0f0", font=("Helvetica", 12))
        self.urun_adı_etiket.pack()
        self.urun_adı_giris = tk.Entry(urun_ekle_pencere)
        self.urun_adı_giris.pack()

        self.urun_fiyatı_etiket = tk.Label(urun_ekle_pencere, text="Bilet Fiyatı:", bg="#f0f0f0", font=("Helvetica", 12))
        self.urun_fiyatı_etiket.pack()
        self.urun_fiyatı_giris = tk.Entry(urun_ekle_pencere)
        self.urun_fiyatı_giris.pack()

        self.urun_adeti_etiket = tk.Label(urun_ekle_pencere, text="Bilet Sayısı:", bg="#f0f0f0", font=("Helvetica", 12))
        self.urun_adeti_etiket.pack()
        self.urun_adeti_giris = tk.Entry(urun_ekle_pencere)
        self.urun_adeti_giris.pack()

        ekle_butonu = tk.Button(urun_ekle_pencere, text="Etkinlik Ekle", command=self.urun_ekle_kaydet, bg="#0c8081", fg="white", font=("Helvetica", 12))
        ekle_butonu.pack(pady=10, padx=20, ipadx=10, ipady=5)

    def urun_ekle_kaydet(self):
        urun_adı = self.urun_adı_giris.get()
        urun_fiyatı = float(self.urun_fiyatı_giris.get())
        urun_adeti = int(self.urun_adeti_giris.get())

        yeni_urun = Urun(ad=urun_adı, fiyat=urun_fiyatı, stok=urun_adeti)
        self.restoran.menu.append(yeni_urun)

        messagebox.showinfo("Başarılı", "Etkinlik başarıyla eklendi.")

    def stok_guncelle(self):
        stok_guncelle_pencere = tk.Toplevel(self.yonetici_pencere)
        stok_guncelle_pencere.title("Bilet Güncelle")

        urunler = [urun.ad for urun in self.restoran.menu]

        self.urun_secim_etiket = tk.Label(stok_guncelle_pencere, text="Etkinlik Seçiniz:", bg="#f0f0f0", font=("Helvetica", 12))
        self.urun_secim_etiket.pack()

        self.urun_secim = tk.StringVar(stok_guncelle_pencere)
        self.urun_secim.set(urunler[0])

        urun_secenekleri = tk.OptionMenu(stok_guncelle_pencere, self.urun_secim, *urunler)
        urun_secenekleri.config(bg="#0c8081", fg="white", font=("Helvetica", 12))
        urun_secenekleri.pack(pady=5, padx=10, ipadx=5, ipady=3)

        self.stok_miktari_etiket = tk.Label(stok_guncelle_pencere, text="Bilet Sayısı:", bg="#f0f0f0", font=("Helvetica", 12))
        self.stok_miktari_etiket.pack()
        self.stok_miktari_giris = tk.Entry(stok_guncelle_pencere)
        self.stok_miktari_giris.pack()

        guncelle_butonu = tk.Button(stok_guncelle_pencere, text="Güncelle", command=self.stok_guncelle_kaydet, bg="#0c8081", fg="white", font=("Helvetica", 12))
        guncelle_butonu.pack(pady=10, padx=20, ipadx=10, ipady=5)

    def stok_guncelle_kaydet(self):
        secilen_urun_ad = self.urun_secim.get()
        stok_miktari = int(self.stok_miktari_giris.get())

        for urun in self.restoran.menu:
            if urun.ad == secilen_urun_ad:
                urun.stok += stok_miktari
                messagebox.showinfo("Başarılı", "Bilet sayısı güncellendi.")
                break

    def fiyat_duzenle(self):
        fiyat_duzenle_pencere = tk.Toplevel(self.yonetici_pencere)
        fiyat_duzenle_pencere.title("Fiyat Düzenle")

        urunler = [urun.ad for urun in self.restoran.menu]

        self.urun_secim_etiket = tk.Label(fiyat_duzenle_pencere, text="Etkinlik Seçiniz:", bg="#f0f0f0", font=("Helvetica", 12))
        self.urun_secim_etiket.pack()

        self.urun_secim = tk.StringVar(fiyat_duzenle_pencere)
        self.urun_secim.set(urunler[0])

        urun_secenekleri = tk.OptionMenu(fiyat_duzenle_pencere, self.urun_secim, *urunler)
        urun_secenekleri.config(bg="#0c8081", fg="white", font=("Helvetica", 12))
        urun_secenekleri.pack(pady=5, padx=10, ipadx=5, ipady=3)

        self.yeni_fiyat_etiket = tk.Label(fiyat_duzenle_pencere, text="Yeni Fiyat:", bg="#f0f0f0", font=("Helvetica", 12))
        self.yeni_fiyat_etiket.pack()
        self.yeni_fiyat_giris = tk.Entry(fiyat_duzenle_pencere)
        self.yeni_fiyat_giris.pack()

        duzenle_butonu = tk.Button(fiyat_duzenle_pencere, text="Düzenle", command=self.fiyat_duzenle_kaydet, bg="#0c8081", fg="white", font=("Helvetica", 12))
        duzenle_butonu.pack(pady=10, padx=20, ipadx=10, ipady=5)

    def fiyat_duzenle_kaydet(self):
        secilen_urun_ad = self.urun_secim.get()
        yeni_fiyat = float(self.yeni_fiyat_giris.get())

        for urun in self.restoran.menu:
            if urun.ad == secilen_urun_ad:
                urun.fiyat = yeni_fiyat
                messagebox.showinfo("Başarılı", "Fiyat güncellendi.")
                break

ana_pencere = tk.Tk()
giris_ekrani = GirisEkrani(ana_pencere)
ana_pencere.mainloop()
