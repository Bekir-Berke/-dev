import arac,musteri, json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

liste = []
arac1 = arac.Arac(1, "Mercedes","C200d","Otomatik","Dizel", 2020, "Boşta", 500)
arac2 = arac.Arac(2, "Audi","A3","Otomatik","Benzin", 2019, "Boşta", 400)
arac3 = arac.Arac(3, "BMW","320i","Otomatik","Benzin", 2018, "Boşta", 450)
arac4 = arac.Arac(4, "Renault","Clio","Manuel","Dizel", 2017, "Boşta", 300)
arac5 = arac.Arac(5, "Fiat","Egea","Manuel","Dizel", 2016, "Boşta", 350)
arac6 = arac.Arac(6, "Hyundai","i20","Manuel","Benzin", 2015, "Boşta", 250)
arac7 = arac.Arac(8, "Volkswagen","Polo","Otomatik","Benzin", 2016, "Boşta", 350)
liste.append(arac1)
liste.append(arac2)
liste.append(arac3)
liste.append(arac4)
liste.append(arac5)
liste.append(arac6)
liste.append(arac7)


def giris_kontrol():
    tel_no = kullanici_adi_entry.get()
    sifre = sifre_entry.get()
    with open("giris.json", "r") as file:
        data = json.load(file)
        for kullanici in data["kullanıcılar"]:
            if kullanici["telefon"] == tel_no and kullanici["sifre"] == sifre:
                messagebox.showinfo("Başarılı", "Giriş Başarılı!")
                ana_ekran(tel_no)
                root.destroy()
                return
        messagebox.showerror("Hata", "Kullanıcı adı veya şifre hatalı!")


def kayıt_ol():
    kayit_ekran = tk.Tk()
    kayit_ekran.title("Kayıt Ol")
    kayit_ekran.geometry("300x200")
    kayit_ekran.resizable(False, False)

    ad_label = tk.Label(kayit_ekran, text="Ad:")
    ad_label.grid(row=0, column=0, padx=10, pady=5)
    ad_entry = tk.Entry(kayit_ekran)
    ad_entry.grid(row=0, column=1, padx=10, pady=5)

    soyad_label = tk.Label(kayit_ekran, text="Soyad:")
    soyad_label.grid(row=1, column=0, padx=10, pady=5)
    soyad_entry = tk.Entry(kayit_ekran)
    soyad_entry.grid(row=1, column=1, padx=10, pady=5)

    telefon_label = tk.Label(kayit_ekran, text="Telefon:")
    telefon_label.grid(row=2, column=0, padx=10, pady=5)
    telefon_entry = tk.Entry(kayit_ekran)
    telefon_entry.grid(row=2, column=1, padx=10, pady=5)

    sifre_label = tk.Label(kayit_ekran, text="Şifre:")
    sifre_label.grid(row=3, column=0, padx=10, pady=5)
    sifre_entry = tk.Entry(kayit_ekran, show="*")
    sifre_entry.grid(row=3, column=1, padx=10, pady=5)


    def kaydet():
        ad = ad_entry.get()
        soyad = soyad_entry.get()
        telefon = telefon_entry.get()
        sifre = sifre_entry.get()
        with open("giris.json", "r") as file:
            data = json.load(file)
            if not any(kullanici["telefon"] == telefon for kullanici in data["kullanıcılar"]):
                data["kullanıcılar"].append({"ad": ad, "soyad": soyad, "telefon": telefon, "sifre": sifre, "arac": []})
                with open("giris.json", "w") as file:
                    json.dump(data, file)
                messagebox.showinfo("Başarılı", "Kayıt Başarılı!")
                kayit_ekran.destroy()
            else:
                messagebox.showerror("Hata", "Bu telefon numarası zaten kayıtlı!")

    kaydet_button = tk.Button(kayit_ekran, text="Kaydet", command=kaydet)
    kaydet_button.grid(row=4, columnspan=3, padx=10, pady=10)
    kayit_ekran.mainloop()
def ana_ekran(tel_no):
    root = tk.Tk()
    root.title("Araç Kiralama")
    root.geometry("400x300")
    root.resizable(False, False)
    with open("giris.json", "r") as file:
        data = json.load(file)
        for kullanici in data["kullanıcılar"]:
            if kullanici["telefon"] == tel_no:
                musteri = kullanici
                break

    def listele():
        liste_pencere = tk.Tk()
        liste_pencere.title("Araç Listesi")
        liste_pencere.geometry("600x400")
        liste_pencere.resizable(False, False)

        araclar_tablo = ttk.Treeview(liste_pencere)
        araclar_tablo["columns"] = (
        "ID", "Marka", "Model", "Vites", "Yakıt", "Yıl", "Fiyat", "Durum")
        araclar_tablo.column("#0", width=0, stretch=tk.NO)
        araclar_tablo.column("ID", anchor=tk.W, width=40)
        araclar_tablo.column("Marka", anchor=tk.W, width=100)
        araclar_tablo.column("Model", anchor=tk.W, width=100)
        araclar_tablo.column("Vites", anchor=tk.W, width=100)
        araclar_tablo.column("Yakıt", anchor=tk.W, width=100)
        araclar_tablo.column("Yıl", anchor=tk.W, width=100)
        araclar_tablo.column("Fiyat", anchor=tk.W, width=100)
        araclar_tablo.column("Durum", anchor=tk.W, width=100)

        araclar_tablo.heading("#0", text="", anchor=tk.W)
        araclar_tablo.heading("ID", text="ID", anchor=tk.W)
        araclar_tablo.heading("Marka", text="Marka", anchor=tk.W)
        araclar_tablo.heading("Model", text="Model", anchor=tk.W)
        araclar_tablo.heading("Vites", text="Vites", anchor=tk.W)
        araclar_tablo.heading("Yakıt", text="Yakıt", anchor=tk.W)
        araclar_tablo.heading("Yıl", text="Yıl", anchor=tk.W)
        araclar_tablo.heading("Fiyat", text="Fiyat", anchor=tk.W)
        araclar_tablo.heading("Durum", text="Durum", anchor=tk.W)

        araclar_tablo.pack(pady=10)

        for arac in liste:
            araclar_tablo.insert("", "end",values=(arac.id, arac.marka, arac.model, arac.vites, arac.yakit, arac.yil, arac.fiyat, arac.kiralama))
        def kirala():
                selected_item = araclar_tablo.selection()[0]
                selected_arac_id = araclar_tablo.item(selected_item)['values'][0]
                for arac in liste:
                    if arac.id == selected_arac_id:
                        if arac.kiralama == "Kiralandı":
                            messagebox.showerror("Hata", "Araç daha önceden kiralanmış!")
                        else:
                            with open("giris.json", "r") as file:
                                data = json.load(file)
                                for kullanici in data["kullanıcılar"]:
                                    if kullanici["telefon"] == tel_no:
                                        d = {
                                            "id": arac.id,
                                            "marka": arac.marka,
                                            "model": arac.model,
                                            "vites": arac.vites,
                                            "yakit": arac.yakit,
                                            "yil": arac.yil,
                                            "kiralama": "Kiralandı"
                                        }
                                        kullanici["arac"].append(d)
                                        break
                            with open("giris.json", "w") as file:
                                json.dump(data, file)

                            arac.durum_güncelle("Kiralandı")
                            messagebox.showinfo("Başarılı", f"{arac.model} aracı kiralandı!")

                araclar_tablo.delete(*araclar_tablo.get_children())
                for arac in liste:
                    araclar_tablo.insert("", "end", values=(
                    arac.id, arac.marka, arac.model, arac.vites, arac.yakit, arac.yil, arac.kiralama))

        kirala_button = tk.Button(liste_pencere, text="Kirala", command=kirala)
        kirala_button.pack()

    listele_button = tk.Button(root, text="Araçları Listele", command=listele)
    listele_button.pack()

    def iptal_et():
        with open("giris.json", "r") as file:
            data = json.load(file)
            for kullanici in data["kullanıcılar"]:
                if kullanici["telefon"] == tel_no:
                    if not kullanici["arac"]:
                        messagebox.showerror("Hata", "Henüz araç kiralamadınız!")
                        return
                    break
        arac=""
        iptal_pencere = tk.Tk()
        iptal_pencere.title("Kiralama İptal")
        iptal_pencere.geometry("300x200")
        iptal_pencere.resizable(False, False)
        with open("giris.json", "r") as file:
            data = json.load(file)
            for kullanici in data["kullanıcılar"]:
                if kullanici["telefon"] == tel_no:
                    arac = kullanici["arac"]
                    break
            arac_text = tk.Text(iptal_pencere, width=40, height=10)
            arac_text.grid(row=0, column=0, padx=5, pady=5)
            arac_text.insert(tk.END, f"Kiralanan Araç:\n")
            arac_text.insert(tk.END, f"Marka: {arac[0]['marka']}\n")
            arac_text.insert(tk.END, f"Model: {arac[0]['model']}\n")
            arac_text.insert(tk.END, f"Vites: {arac[0]['vites']}\n")
            arac_text.insert(tk.END, f"Yakıt: {arac[0]['yakit']}\n")
            arac_text.insert(tk.END, f"Yıl: {arac[0]['yil']}\n")

        def iptal_et_func():
            with open("giris.json", "r") as file:
                data = json.load(file)
                for kullanici in data["kullanıcılar"]:
                    if kullanici["telefon"] == tel_no:
                        kullanici["arac"] = []
                        break
            with open("giris.json", "w") as file:
                json.dump(data, file)
            messagebox.showinfo("Başarılı", "Kiralama İptal Edildi!")
            iptal_pencere.destroy()

        iptal_button = tk.Button(iptal_pencere, text="İptal Et", command=iptal_et_func)
        iptal_button.grid(row=1, columnspan=2, padx=10, pady=10)
        iptal_pencere.mainloop()


    iptal_button = tk.Button(root, text="Kiralama Bilgisi", command=iptal_et)
    iptal_button.pack()



root = tk.Tk()
root.title("Giriş Ekranı")

kullanici_adi_label = tk.Label(root, text="Telefon Numarası:")
kullanici_adi_label.grid(row=0, column=0, padx=10, pady=5)
kullanici_adi_entry = tk.Entry(root)
kullanici_adi_entry.grid(row=0, column=1, padx=10, pady=5)

sifre_label = tk.Label(root, text="Şifre:")
sifre_label.grid(row=1, column=0, padx=10, pady=5)
sifre_entry = tk.Entry(root, show="*")
sifre_entry.grid(row=1, column=1, padx=10, pady=5)

giris_button = tk.Button(root, text="Giriş Yap", command=giris_kontrol)
giris_button.grid(row=2, columnspan=2, padx=10, pady=10)
kayıt_button = tk.Button(root, text="Kayıt Ol", command=kayıt_ol)
kayıt_button.grid(row=2, column=2, padx=10, pady=10)
root.mainloop()

