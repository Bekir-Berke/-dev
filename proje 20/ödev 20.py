import tkinter as tk
from tkinter import ttk, messagebox

class Oyun:
    def __init__(self, adi, turu, platformu):
        self.adi = adi
        self.turu = turu
        self.platformu = platformu
        self.degerlendirme = None  # Her oyun için ayrı bir degerlendirme değeri


class Koleksiyon:
    def __init__(self):
        self.oyunlar = []

    def oyun_ekle(self, oyun):
        if oyun not in self.oyunlar:
            self.oyunlar.append(oyun)
            return True
        else:
            return False

    def oyunlari_listele(self):
        return self.oyunlar

class Oyuncu:
    def __init__(self, adi, koleksiyon=None):
        self.adi = adi
        self.favori_oyunlar = []
        self.koleksiyon = koleksiyon if koleksiyon else Koleksiyon()

    def oyun_degerlendir(self, oyun, degerlendirme):
        if degerlendirme:
            oyun.degerlendirme = degerlendirme
            messagebox.showinfo("Başarılı", f"{oyun.adi} oyununa {degerlendirme} olarak değerlendirildi!")
        else:
            messagebox.showerror("Hata", "Lütfen bir değerlendirme seçin!")

oyuncu = Oyuncu("oyuncu")

def oyun_ekle():
    ad = oyun_adi_entry.get()
    tur = oyun_turu_entry.get()
    platform = oyun_platformu_entry.get()
    if ad and tur and platform:
        oyun = Oyun(ad, tur, platform)  # Her oyun için yeni bir Oyun nesnesi oluştur
        if oyuncu.koleksiyon.oyun_ekle(oyun):
            update_oyun_listesi()  # Yeni oyun eklendiğinde listeyi güncelle
            messagebox.showinfo("Başarılı", "Oyun koleksiyonunuza eklendi!")
        else:
            messagebox.showerror("Hata", "Bu oyun zaten koleksiyonunuzda bulunuyor!")
    else:
        messagebox.showerror("Hata", "Lütfen tüm alanları doldurun!")


def oyun_sil():
    secili_item = oyun_listesi.selection()
    if secili_item:
        secili_oyun = oyun_listesi.item(secili_item)["values"]
        oyun_adi = secili_oyun[0]
        for oyun in oyuncu.koleksiyon.oyunlar:
            if oyun.adi == oyun_adi:
                oyuncu.koleksiyon.oyunlar.remove(oyun)  # Koleksiyondan da sil
                update_oyun_listesi()  # Güncel listeyi göster
                messagebox.showinfo("Başarılı", f"{oyun.adi} oyunu koleksiyonunuzdan silindi!")
                return
    else:
        messagebox.showerror("Hata", "Lütfen bir oyun seçin!")

def degerlendir(oyun_adi_entry, degerlendirme_entry):
        oyun_adi = oyun_adi_entry.get()
        degerlendirme = degerlendirme_entry.get()
        
        # Girilen değerin 0-5 aralığında olup olmadığını kontrol ediyoruz
        try:
            degerlendirme = float(degerlendirme)
            if 0 <= degerlendirme <= 5:
                degerlendirme = int(degerlendirme)  # Puanı tam sayıya dönüştür
                for oyun in oyuncu.koleksiyon.oyunlar:
                    if oyun.adi == oyun_adi:
                        oyuncu.oyun_degerlendir(oyun, degerlendirme)
                        update_oyun_listesi()  # Değerlendirme yapıldığında liste güncellenmeli
                        return
                messagebox.showerror("Hata", "Lütfen bir oyun seçin!")
            else:
                messagebox.showerror("Hata", "Lütfen 0-5 arası bir rakam giriniz!")
        except ValueError:
            messagebox.showerror("Hata", "Lütfen sayısal bir değer girin!")
    
    

def update_oyun_listesi():
    oyun_listesi.delete(*oyun_listesi.get_children())
    for oyun in oyuncu.koleksiyon.oyunlar:
        degerlendirme = oyun.degerlendirme if oyun.degerlendirme is not None else "Henüz değerlendirilmedi"
        row_values = (oyun.adi, oyun.turu, oyun.platformu, degerlendirme)
        oyun_listesi.insert("", "end", values=row_values)

def kayit_ol():
    kullanici_adi = kullanici_adi_entry.get()
    sifre = sifre_entry.get()
    if kullanici_adi and sifre:
        with open("kullanicilar.txt", "a") as file:
            file.write(f"{kullanici_adi},{sifre}\n")
        messagebox.showinfo("Başarılı", "Kayıt işlemi başarıyla tamamlandı!")
    else:
        messagebox.showerror("Hata", "Lütfen kullanıcı adı ve şifre alanlarını doldurun!")

def giris():
    kullanici_adi = kullanici_adi_entry.get()
    sifre = sifre_entry.get()
    with open("kullanicilar.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(",")
            if kullanici_adi == stored_username and sifre == stored_password:
                messagebox.showinfo("Başarılı", "Giriş başarılı!")
                giris_root.destroy()  # Giriş penceresini kapat
                ana_arayuze_gec()  # Ana arayü        geçiş fonksiyonunu çağır
                return
    messagebox.showerror("Hata", "Geçersiz kullanıcı adı veya şifre!")

def ana_arayuze_gec():
    global root
    root = tk.Tk()
    root.title("Oyun Koleksiyonu Yönetimi")

    frame = tk.Frame(root, bg="#f0f0f0")
    frame.pack(padx=20, pady=20)

    oyun_adi_label = tk.Label(frame, text="Oyun Adı:", bg="#f0f0f0")
    oyun_adi_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    global oyun_adi_entry
    oyun_adi_entry = tk.Entry(frame)
    oyun_adi_entry.grid(row=0, column=1, padx=5, pady=5)

    oyun_turu_label = tk.Label(frame, text="Oyun Türü:", bg="#f0f0f0")
    oyun_turu_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    global oyun_turu_entry
    oyun_turu_entry = tk.Entry(frame)
    oyun_turu_entry.grid(row=1, column=1, padx=5, pady=5)

    oyun_platformu_label = tk.Label(frame, text="Oyun Platformu:", bg="#f0f0f0")
    oyun_platformu_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    global oyun_platformu_entry
    oyun_platformu_entry = tk.Entry(frame)
    oyun_platformu_entry.grid(row=2, column=1, padx=5, pady=5)

    oyun_ekle_button = tk.Button(frame, text="Oyun Ekle", command=oyun_ekle, bg="#4CAF50", fg="white")
    oyun_ekle_button.grid(row=3, column=0, padx=5, pady=5, sticky="we")

    oyun_sil_button = tk.Button(frame, text="Oyunu Sil", command=oyun_sil, bg="#FF5733", fg="white")
    oyun_sil_button.grid(row=3, column=1, padx=5, pady=5, sticky="we")

    oyun_listesi_label = tk.Label(frame, text="Koleksiyonunuz:", bg="#f0f0f0")
    oyun_listesi_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="w")

    global oyun_listesi
    oyun_listesi = ttk.Treeview(frame, columns=("Adı", "Türü", "Platformu", "Değerlendirme"), show="headings", selectmode="browse")
    oyun_listesi.heading("Adı", text="Oyun Adı")
    oyun_listesi.heading("Türü", text="Tür")
    oyun_listesi.heading("Platformu", text="Platform")
    oyun_listesi.heading("Değerlendirme", text="Değerlendirme")
    oyun_listesi.column("Adı", width=150)
    oyun_listesi.column("Türü", width=100)
    oyun_listesi.column("Platformu", width=100)
    oyun_listesi.column("Değerlendirme", width=100)
    oyun_listesi.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    # Değerlendirme alanını ekleyelim
    degerlendirme_label = tk.Label(frame, text="Değerlendirme (0-5 arası):", bg="#f0f0f0")
    degerlendirme_label.grid(row=6, column=0, padx=5, pady=5, sticky="e")

    global degerlendirme_entry
    degerlendirme_entry = tk.Entry(frame)
    degerlendirme_entry.grid(row=6, column=1, padx=5, pady=5)

    degerlendir_button = tk.Button(frame, text="Değerlendir", command=lambda: degerlendir(oyun_adi_entry, degerlendirme_entry), bg="#FFC107", fg="white")
    degerlendir_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    update_oyun_listesi()

    root.mainloop()

def kullanici_kontrol():
    global giris_root
    giris_root = tk.Tk()
    giris_root.title("Kullanıcı Girişi")

    giris_frame = tk.Frame(giris_root, bg="#f0f0f0")
    giris_frame.pack(padx=20, pady=20)

    kullanici_adi_label = tk.Label(giris_frame, text="Kullanıcı Adı:", bg="#f0f0f0")
    kullanici_adi_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

    global kullanici_adi_entry
    kullanici_adi_entry = tk.Entry(giris_frame)
    kullanici_adi_entry.grid(row=0, column=1, padx=5, pady=5)

    sifre_label = tk.Label(giris_frame, text="Şifre:", bg="#f0f0f0")
    sifre_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

    global sifre_entry
    sifre_entry = tk.Entry(giris_frame, show="*")
    sifre_entry.grid(row=1, column=1, padx=5, pady=5)

    kayit_ol_button = tk.Button(giris_frame, text="Kayıt Ol", command=kayit_ol, bg="#2196F3", fg="white")
    kayit_ol_button.grid(row=2, column=0, padx=5, pady=5, sticky="we")

    giris_button = tk.Button(giris_frame, text="Giriş Yap", command=giris, bg="#4CAF50", fg="white")
    giris_button.grid(row=2, column=1, padx=5, pady=5, sticky="we")

    giris_root.mainloop()

kullanici_kontrol()
