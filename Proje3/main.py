import Kitap, Uye, Odunc, kutuphane
import tkinter as tk
from tkinter import messagebox


class KütüphaneGUI:
    def __init__(self, root):
        self.root = root

        self.kutuphane = kutuphane.Kutuphane()
        self.frame = tk.Frame(root)
        self.frame.pack(expand=True)

        self.label = tk.Label(self.frame, text="Kütüphane Yönetim Sistemi", font=("Helvetica", 16))
        self.label.pack(pady=(10, 0))

        self.button_kitap_ekle = tk.Button(self.frame, text="Kitap Ekle", command=self.kitap_ekle)
        self.button_kitap_ekle.pack(pady=5)

        self.button_uye_ekle = tk.Button(self.frame, text="Üye Ekle", command=self.uye_ekle)
        self.button_uye_ekle.pack(pady=5)

        self.button_odunc_al = tk.Button(self.frame, text="Kitap Ödünç Al", command=self.kitap_odunc_al)
        self.button_odunc_al.pack(pady=5)

        self.button_iade_et = tk.Button(self.frame, text="Kitap İade Et", command=self.kitap_iade_et)
        self.button_iade_et.pack(pady=5)

        self.button_odunc_bilgisi = tk.Button(self.frame, text="Ödünç Bilgisi", command=self.odunc_bilgisi)
        self.button_odunc_bilgisi.pack(pady=10)

        self.button_kitaplari_listele = tk.Button(self.frame, text="Kitapları Listele", command=self.kitaplari_listele)
        self.button_kitaplari_listele.pack(pady=10)

        self.button_cikis = tk.Button(self.frame, text="Çıkış", command=self.root.quit)
        self.button_cikis.pack(pady=10)


    def kitap_ekle(self):
        kitap_ekle_pencere = tk.Toplevel(self.root)
        kitap_ekle_pencere.title("Kitap Ekle")

        label_isbn = tk.Label(kitap_ekle_pencere, text="ISBN:")
        label_isbn.grid(row=0, column=0, padx=5, pady=5)
        entry_isbn = tk.Entry(kitap_ekle_pencere)
        entry_isbn.grid(row=0, column=1, padx=5, pady=5)

        label_ad = tk.Label(kitap_ekle_pencere, text="Ad:")
        label_ad.grid(row=1, column=0, padx=5, pady=5)
        entry_ad = tk.Entry(kitap_ekle_pencere)
        entry_ad.grid(row=1, column=1, padx=5, pady=5)

        label_yazar = tk.Label(kitap_ekle_pencere, text="Yazar:")
        label_yazar.grid(row=2, column=0, padx=5, pady=5)
        entry_yazar = tk.Entry(kitap_ekle_pencere)
        entry_yazar.grid(row=2, column=1, padx=5, pady=5)

        def kitap_ekle_func():
            isbn = entry_isbn.get()
            ad = entry_ad.get()
            yazar = entry_yazar.get()
            kitap = Kitap.Kitap(isbn, ad, yazar)
            self.kutuphane.kitap_ekle(kitap)
            messagebox.showinfo("Başarılı", "Kitap başarıyla eklendi.")
            kitap_ekle_pencere.destroy()

        button_ekle = tk.Button(kitap_ekle_pencere, text="Ekle", command=kitap_ekle_func)
        button_ekle.grid(row=3, column=0, columnspan=2, pady=10)

    def uye_ekle(self):
        uye_ekle_pencere = tk.Toplevel(self.root)
        uye_ekle_pencere.title("Üye Ekle")

        label_id = tk.Label(uye_ekle_pencere, text="Üye ID:")
        label_id.grid(row=0, column=0, padx=5, pady=5)
        entry_id = tk.Entry(uye_ekle_pencere)
        entry_id.grid(row=0, column=1, padx=5, pady=5)

        label_ad = tk.Label(uye_ekle_pencere, text="Ad:")
        label_ad.grid(row=1, column=0, padx=5, pady=5)
        entry_ad = tk.Entry(uye_ekle_pencere)
        entry_ad.grid(row=1, column=1, padx=5, pady=5)

        label_soyad = tk.Label(uye_ekle_pencere, text="Soyad:")
        label_soyad.grid(row=2, column=0, padx=5, pady=5)
        entry_soyad = tk.Entry(uye_ekle_pencere)
        entry_soyad.grid(row=2, column=1, padx=5, pady=5)

        def uye_ekle_func():
            uye_id = entry_id.get()
            ad = entry_ad.get()
            soyad = entry_soyad.get()
            uye = Uye.Uye(uye_id, ad, soyad)
            self.kutuphane.uye_ekle(uye)
            messagebox.showinfo("Başarılı", "Üye başarıyla eklendi.")
            uye_ekle_pencere.destroy()

        button_ekle = tk.Button(uye_ekle_pencere, text="Ekle", command=uye_ekle_func)
        button_ekle.grid(row=3, column=0, columnspan=2, pady=10)

    def kitap_odunc_al(self):
        kitap_odunc_pencere = tk.Toplevel(self.root)
        kitap_odunc_pencere.title("Kitap Ödünç Al")

        label_kitap_id = tk.Label(kitap_odunc_pencere, text="Kitap ID:")
        label_kitap_id.grid(row=0, column=0, padx=5, pady=5)
        entry_kitap_id = tk.Entry(kitap_odunc_pencere)
        entry_kitap_id.grid(row=0, column=1, padx=5, pady=5)

        label_uye_id = tk.Label(kitap_odunc_pencere, text="Üye ID:")
        label_uye_id.grid(row=1, column=0, padx=5, pady=5)
        entry_uye_id = tk.Entry(kitap_odunc_pencere)
        entry_uye_id.grid(row=1, column=1, padx=5, pady=5)

        def kitap_odunc_func():
            kitap_id = entry_kitap_id.get()
            uye_id = entry_uye_id.get()
            message = self.kutuphane.odunc_al(kitap_id, uye_id)
            messagebox.showinfo("Bilgi", message)
            kitap_odunc_pencere.destroy()

        button_odunc_al = tk.Button(kitap_odunc_pencere, text="Ödünç Al", command=kitap_odunc_func)
        button_odunc_al.grid(row=2, column=0, columnspan=2, pady=10)

    def kitap_iade_et(self):
        kitap_iade_pencere = tk.Toplevel(self.root)
        kitap_iade_pencere.title("Kitap İade Et")

        label_kitap_id = tk.Label(kitap_iade_pencere, text="Kitap ID:")
        label_kitap_id.grid(row=0, column=0, padx=5, pady=5)
        entry_kitap_id = tk.Entry(kitap_iade_pencere)
        entry_kitap_id.grid(row=0, column=1, padx=5, pady=5)

        def kitap_iade_func():
            kitap_id = entry_kitap_id.get()
            message = self.kutuphane.iade_et(kitap_id)
            messagebox.showinfo("Bilgi", message)
            kitap_iade_pencere.destroy()

        button_iade_et = tk.Button(kitap_iade_pencere, text="İade Et", command=kitap_iade_func)
        button_iade_et.grid(row=1, column=0, columnspan=2, pady=10)

    def odunc_bilgisi(self):
        odunc_bilgisi_pencere = tk.Toplevel(self.root)
        odunc_bilgisi_pencere.title("Ödünç Bilgisi")

        text = tk.Text(odunc_bilgisi_pencere, width=40, height=10)
        text.grid(row=0, column=0, padx=5, pady=5)

        for odunc in self.kutuphane.odunc_islemleri:
            text.insert(tk.END, odunc.odunc_bilgisi() + "\n")

        text.config(state=tk.DISABLED)

    def kitaplari_listele(self):
        kitap_listele_pencere = tk.Toplevel(self.root)
        kitap_listele_pencere.title("Kitapları Listele")

        label_baslik = tk.Label(kitap_listele_pencere, text="Kitaplar", font=("Helvetica", 14, "bold"))
        label_baslik.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        text = tk.Text(kitap_listele_pencere, width=60, height=10)
        text.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        for kitap in self.kutuphane.kitaplar:
            text.insert(tk.END, f"Kitap ID: {kitap.kitap_id}\n")
            text.insert(tk.END, f"Ad: {kitap.ad}\n")
            text.insert(tk.END, f"Yazar: {kitap.yazar}\n")
            text.insert(tk.END, f"Durum: {kitap.durum}\n")
            text.insert(tk.END, "-" * 30 + "\n")

        text.config(state=tk.DISABLED)


def main():
    root = tk.Tk()
    root.title("Kütüphane Yönetim Sistemi")

    window_width = 800
    window_height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    app = KütüphaneGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
