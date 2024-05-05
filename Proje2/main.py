from doktor import Doktor
from hasta import Hasta
from randevu import Randevu
import tkinter as tk
import datetime
from tkcalendar import Calendar
from tkinter import ttk
from tkinter import messagebox
import json


doktorlar = []
doktor1 = Doktor("Dr. Ahmet", "Dahiliye", "Müsait Değil")
doktor2 = Doktor("Dr. Mehmet", "KBB")
doktor3 = Doktor("Dr. Ayşe", "Göz")
doktor4 = Doktor("Dr. Fatma", "Kalp")

doktorlar.append(doktor1)
doktorlar.append(doktor2)
doktorlar.append(doktor3)
doktorlar.append(doktor4)

class TCNoGirisEkrani:
    def __init__(self, root):
        self.root = root
        self.root.title("Giriş Ekranı")
        self.root.resizable(False, False)

        self.label_tc_no = tk.Label(root, text="TC Kimlik Numarası:")
        self.label_tc_no.grid(row=0, column=0, pady=5)
        self.entry_tc_no = tk.Entry(root)
        self.entry_tc_no.grid(row=0, column=1, pady=5)

        self.label_ad = tk.Label(root, text="Ad:")
        self.label_ad.grid(row=1, column=0, pady=5)
        self.entry_ad = tk.Entry(root)
        self.entry_ad.grid(row=1, column=1, pady=5)

        self.label_soyad = tk.Label(root, text="Soyad:")
        self.label_soyad.grid(row=2, column=0, pady=5)
        self.entry_soyad = tk.Entry(root)
        self.entry_soyad.grid(row=2, column=1, pady=5)

        self.label_yas = tk.Label(root, text="Yaş:")
        self.label_yas.grid(row=3, column=0, pady=5)
        self.entry_yas = tk.Entry(root)
        self.entry_yas.grid(row=3, column=1, pady=5)

        self.cinsiyet = tk.StringVar()
        self.label_cinsiyet = tk.Label(root, text="Cinsiyet:")
        self.label_cinsiyet.grid(row=4, column=0, pady=5)
        self.radio_erkek = tk.Radiobutton(root, text="Erkek", variable=self.cinsiyet, value="E")
        self.radio_erkek.grid(row=4, column=1, pady=5)
        self.radio_kadin = tk.Radiobutton(root, text="Kadın", variable=self.cinsiyet, value="K")
        self.radio_kadin.grid(row=4, column=2, pady=5)

        self.button_giris = tk.Button(root, text="Giriş Yap", command=self.giris_kontrol, width=10)
        self.button_giris.grid(row=5, column=0, columnspan=2, pady=5)


    def giris_kontrol(self):
        tc_no = self.entry_tc_no.get()

        if len(tc_no) < 11:
            messagebox.showerror("Hata", "TC Kimlik numarası 11 haneli olmalıdır.")
        elif not tc_no.isdigit():
            messagebox.showerror("Hata", "TC Kimlik numarası sadece rakamlardan oluşmalıdır.")
        else:
            self.randevu_sistemi_ac()

    def randevu_sistemi_ac(self):
        with open("hasta_bilgileri.json", "r") as file:
            data = json.load(file)
            tc_no = self.entry_tc_no.get()
            ad = self.entry_ad.get()
            soyad = self.entry_soyad.get()
            yas = self.entry_yas.get()
            cinsiyet = self.cinsiyet.get()

            if not data["kullanıcılar"]:
                data["kullanıcılar"].append({
                    "ad": ad,
                    "soyad": soyad,
                    "tc_no": tc_no,
                    "yas": yas,
                    "cinsiyet": cinsiyet,
                    "randevular": []
                })
                with open("hasta_bilgileri.json", "w") as file:
                    file.write(json.dumps(data))
            else:
                for kullanici in data["kullanıcılar"]:
                    if kullanici["tc_no"] == tc_no:
                        if kullanici["ad"] == ad and kullanici["soyad"] == soyad:
                            break
                        else:
                            messagebox.showerror("Hata", "Girilen bilgiler hatalıdır.")
                            return
                    else:
                        messagebox.showerror("Hata", "Girilen TC Kimlik numarası sistemde kayıtlı değildir.")
                        return
        self.root.destroy()
        root = tk.Tk()
        app = RandevuSistemiGUI(root, tc_no)
        root.mainloop()


class RandevuSistemiGUI:
    def __init__(self, root, tc_no):
        with open("hasta_bilgileri.json", "r") as file:
            data = json.load(file)
            for kullanici in data["kullanıcılar"]:
                if kullanici["tc_no"] == tc_no:
                    ad = kullanici["ad"]
                    soyad = kullanici["soyad"]
                    tc_no = kullanici["tc_no"]
                    yas = kullanici["yas"]
                    cinsiyet = kullanici["cinsiyet"]
                    randevular = kullanici["randevular"]
        self.hasta = Hasta(ad, soyad, tc_no, yas, cinsiyet  , randevular)
        print(self.hasta.randevu_gecmisi)
        self.root = root
        self.root.title("Hastane Randevu Sistemi")
        self.root.geometry("400x400")

        self.label = tk.Label(root, text=f"Hoş Geldiniz {self.hasta.ad}", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.button_randevu_al = tk.Button(root, text="Randevu Al", command=self.randevu_al_menu)
        self.button_randevu_al.pack(pady=5)

        self.button_randevu_iptal = tk.Button(root, text="Randevu İptal", command=self.randevu_iptal_menu)
        self.button_randevu_iptal.pack(pady=5)

        self.button_randevular = tk.Button(root, text="Randevularımı Görüntüle", command=self.randevularimi_goruntule_menu)
        self.button_randevular.pack(pady=5)

        self.button_cikis = tk.Button(root, text="Çıkış", command=self.uygulamadan_cikis)
        self.button_cikis.pack(pady=5)

    def uygulamadan_cikis(self):
        self.root.destroy()
        root = tk.Tk()
        app = TCNoGirisEkrani(root)
        root.geometry("400x400")
        root.mainloop()

    def randevularimi_goruntule_menu(self):

        self.randevularimi_goruntule_pencere = tk.Toplevel()
        self.randevularimi_goruntule_pencere.title("Randevularım")

        self.treeview_randevular = ttk.Treeview(self.randevularimi_goruntule_pencere, columns=("Tarih", "Doktor", "Bölüm"), show="headings")
        self.treeview_randevular.heading("Tarih", text="Tarih", anchor="center")
        self.treeview_randevular.heading("Doktor", text="Doktor", anchor="center")
        self.treeview_randevular.heading("Bölüm", text="Bölüm", anchor="center")
        self.treeview_randevular.pack(pady=10)

        for randevu in self.hasta.randevu_gecmisi:
            self.treeview_randevular.insert("", "end", values=(randevu['tarih'], randevu['doktor'], randevu['bolum']))

        self.button_kapat = tk.Button(self.randevularimi_goruntule_pencere, text="Kapat", command=self.randevularimi_goruntule_pencere.destroy)
        self.button_kapat.pack(pady=5)
    def randevu_al_menu(self):
        self.randevu_al_pencere = tk.Toplevel()
        self.randevu_al_pencere.title("Randevu Al")

        self.treeview = ttk.Treeview(self.randevu_al_pencere, columns=("Doktor","Uzmanlık Alanı", "Müsaitlik Durumu"), show="headings")
        self.treeview.heading("Doktor", text="Doktor", anchor="center")
        self.treeview.heading("Uzmanlık Alanı", text="Uzmanlık Alanı", anchor="center")
        self.treeview.heading("Müsaitlik Durumu", text="Müsaitlik Durumu", anchor="center")
        self.treeview.pack(pady=10)

        for doktor in doktorlar:
            self.treeview.insert("", "end", values=(doktor.isim, doktor.uzmanlik_alani, doktor.musaitlik_durumu))
        self.cal = Calendar(self.randevu_al_pencere, selectmode="day", year=2024, month=5, day=5)
        self.cal.pack(pady=10)

        self.button_kapat = tk.Button(self.randevu_al_pencere, text="Randevu al", command=self.randevu_al)
        self.button_kapat.pack(pady=5)

    def randevu_al(self):
        secili_doktor = self.treeview.selection()[0]
        doktor = self.treeview.item(secili_doktor)["values"]
        tarih = self.cal.get_date()
        randevu = None
        if doktor[2] == "Müsait Değil":
            messagebox.showinfo("Hata", "Doktor müsait değil.")
        elif doktor[2] == "Müsait":
            randevu = Randevu(tarih, doktor[0], doktor[1], self.hasta)
            self.hasta.randevu_al(randevu)
            doktor_obj = [d for d in doktorlar if d.isim == doktor[0]][0]
            doktor_obj.musaitlik_degistir("Müsait Değil")
            with open("hasta_bilgileri.json", "r") as file:
                data = json.load(file)
                for kullanici in data["kullanıcılar"]:
                    if kullanici["tc_no"] == self.hasta.tc_no:
                        kullanici["randevular"].append({
                            "tarih": randevu.tarih,
                            "doktor": randevu.doktor,
                            "bolum": randevu.bolum
                        })
                with open("hasta_bilgileri.json", "w") as file:
                    file.write(json.dumps(data))
                messagebox.showinfo("Başarılı", "Randevunuz alınmıştır.")
                self.treeview.delete(*self.treeview.get_children())
                for doktor in doktorlar:
                    self.treeview.insert("", "end", values=(doktor.isim, doktor.uzmanlik_alani, doktor.musaitlik_durumu))
        else:
            messagebox.showinfo("Hata", "Beklenmeyen bir hata oluştu.")
    def randevu_iptal_menu(self):
        self.randevu_iptal_pencere = tk.Toplevel()
        self.randevu_iptal_pencere.title("Randevu İptal")
        self.treeview_iptal = ttk.Treeview(self.randevu_iptal_pencere, columns=("Tarih", "Doktor", "Bölüm"), show="headings")
        self.treeview_iptal.heading("Tarih", text="Tarih", anchor="center")
        self.treeview_iptal.heading("Doktor", text="Doktor", anchor="center")
        self.treeview_iptal.heading("Bölüm", text="Bölüm", anchor="center")

        for randevu in self.hasta.randevu_gecmisi:
            self.treeview_iptal.insert("", "end", values=(randevu['tarih'], randevu['doktor'], randevu['bolum']))
        self.treeview_iptal.pack(pady=10)
        self.button_randevu_iptal = tk.Button(self.randevu_iptal_pencere, text="Randevu İptal", command=self.randevu_iptal)
        self.button_randevu_iptal.pack(pady=5)

    def randevu_iptal(self):
        secili_randevu = self.treeview_iptal.selection()[0]
        randevu = self.treeview_iptal.item(secili_randevu)["values"]
        randevu_obj = [r for r in self.hasta.randevu_gecmisi if r['tarih'] == randevu[0] and r['doktor'] == randevu[1] and r['bolum'] == randevu[2]][0]
        self.hasta.randevu_iptal(randevu_obj)
        doktor_obj = [d for d in doktorlar if d.isim == randevu[1]][0]
        doktor_obj.musaitlik_degistir("Müsait")
        with open("hasta_bilgileri.json", "r") as file:
            data = json.load(file)
            for kullanici in data["kullanıcılar"]:
                if kullanici["tc_no"] == self.hasta.tc_no:
                    kullanici["randevular"].remove({
                        "tarih": randevu_obj['tarih'],
                        "doktor": randevu_obj['doktor'],
                        "bolum": randevu_obj['bolum']
                    })
        with open("hasta_bilgileri.json", "w") as file:
            file.write(json.dumps(data))
        messagebox.showinfo("Başarılı", "Randevunuz iptal edilmiştir.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TCNoGirisEkrani(root)
    root.mainloop()
    root.geometry("400x200")



