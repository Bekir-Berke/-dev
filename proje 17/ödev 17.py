import tkinter as tk
from tkinter import ttk

class EgitimPlatformu:
    def __init__(self, pencere):
        self.pencere = pencere
        self.pencere.title("Eğitim Materyali Paylaşım Platformu")
        self.pencere.geometry("800x600")

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.label_kategori = ttk.Label(pencere, text="Kategori Seçin:", font=("Helvetica", 14))
        self.label_kategori.pack(pady=10)

        self.combobox_kategori = ttk.Combobox(pencere, values=["Python", "Veri Bilimi", "Web Geliştirme", "Matematik"], font=("Helvetica", 12))
        self.combobox_kategori.pack()

        self.btn_listele = ttk.Button(pencere, text="Listele", command=self.listele, style='Accent.TButton')
        self.btn_listele.pack(pady=10)

        self.btn_materyal_ekle = ttk.Button(pencere, text="Materyal Ekle", command=self.materyal_ekle_ekrani_ac, style='Accent.TButton')
        self.btn_materyal_ekle.pack(pady=10)

        self.btn_soru_sor = ttk.Button(pencere, text="Soru Sor", command=self.soru_sor_ekrani_ac, style='Accent.TButton')
        self.btn_soru_sor.pack(pady=10)

        self.btn_sorular = ttk.Button(pencere, text="Sorular", command=self.sorular_listele, style='Accent.TButton')
        self.btn_sorular.pack(pady=10)

        self.materyal_dict = {
            "Python": ["Python Başlangıç Eğitimi", "Python İleri Seviye Eğitimi"],
            "Veri Bilimi": ["Veri Bilimi Temelleri", "Veri Analizi Pratikleri"],
            "Web Geliştirme": ["Web Geliştirme Temelleri", "Django ile Web Uygulama Geliştirme"]
        }  # Her kategoriye ait materyalleri saklayacak sözlük

        self.sorular = {}  # Ders adı ve soruları saklayacak sözlük

        self.liste = tk.Listbox(pencere, width=100, height=20, font=("Helvetica", 12))
        self.liste.pack(pady=20)

    def listele(self):
        secilen_kategori = self.combobox_kategori.get()
        self.liste.delete(0, tk.END)  # Önceki içeriği temizle
        
        if secilen_kategori in self.materyal_dict:
            materyaller = self.materyal_dict[secilen_kategori]
            for materyal in materyaller:
                self.liste.insert(tk.END, materyal)

    def materyal_ekle_ekrani_ac(self):
        self.ekle_pencere = tk.Toplevel(self.pencere)
        self.ekle_pencere.title("Materyal Ekle")
        self.ekle_pencere.geometry("400x300")

        self.label_ders_adi = ttk.Label(self.ekle_pencere, text="Ders Adı:", font=("Helvetica", 14))
        self.label_ders_adi.pack()

        self.entry_ders_adi = ttk.Entry(self.ekle_pencere, font=("Helvetica", 12))
        self.entry_ders_adi.pack()

        self.label_materyal_adi = ttk.Label(self.ekle_pencere, text="Materyal Adı:", font=("Helvetica", 14))
        self.label_materyal_adi.pack()

        self.entry_materyal_adi = ttk.Entry(self.ekle_pencere, font=("Helvetica", 12))
        self.entry_materyal_adi.pack()

        self.label_materyal_icerik = ttk.Label(self.ekle_pencere, text="Materyal İçeriği:", font=("Helvetica", 14))
        self.label_materyal_icerik.pack()

        self.entry_materyal_icerik = tk.Text(self.ekle_pencere, height=10, font=("Helvetica", 12))
        self.entry_materyal_icerik.pack()

        self.btn_ekle = ttk.Button(self.ekle_pencere, text="Ekle", command=self.materyal_ekle, style='Accent.TButton')
        self.btn_ekle.pack(pady=10)

    def materyal_ekle(self):
        ders_adi = self.entry_ders_adi.get()
        materyal_adi = self.entry_materyal_adi.get()
        materyal_icerik = self.entry_materyal_icerik.get("1.0", tk.END)

        secilen_kategori = ders_adi
        if secilen_kategori not in self.materyal_dict:
            self.materyal_dict[secilen_kategori] = []

        self.materyal_dict[secilen_kategori].append(f"{ders_adi} - {materyal_adi}")

        self.combobox_kategori.config(values=list(self.materyal_dict.keys()))

        tk.messagebox.showinfo("Başarılı", "Materyal başarıyla eklendi!")

    def soru_sor_ekrani_ac(self):
        self.soru_sor_pencere = tk.Toplevel(self.pencere)
        self.soru_sor_pencere.title("Soru Sor")
        self.soru_sor_pencere.geometry("400x300")

        self.label_ders_sec = ttk.Label(self.soru_sor_pencere, text="Ders Seçin:", font=("Helvetica", 14))
        self.label_ders_sec.pack()

        self.combobox_ders_sec = ttk.Combobox(self.soru_sor_pencere, values=list(self.materyal_dict.keys()), font=("Helvetica", 12))
        self.combobox_ders_sec.pack()

        self.label_soru = ttk.Label(self.soru_sor_pencere, text="Soru:", font=("Helvetica", 14))
        self.label_soru.pack()

        self.entry_soru = tk.Text(self.soru_sor_pencere, height=10, font=("Helvetica", 12))
        self.entry_soru.pack()

        self.btn_soru_ekle = ttk.Button(self.soru_sor_pencere, text="Sor", command=self.soru_ekle, style='Accent.TButton')
        self.btn_soru_ekle.pack(pady=10)

    def soru_ekle(self):
        secilen_ders = self.combobox_ders_sec.get()
        soru = self.entry_soru.get("1.0", tk.END)

        if secilen_ders not in self.sorular:
            self.sorular[secilen_ders] = []

        self.sorular[secilen_ders].append(soru.strip())

    def sorular_listele(self):
        self.sorular_pencere = tk.Toplevel(self.pencere)
        self.sorular_pencere.title("Sorular")
        self.sorular_pencere.geometry("800x600")

        sorular_frame = tk.Frame(self.sorular_pencere)
        sorular_frame.pack(fill=tk.BOTH, expand=True)

        tree = ttk.Treeview(sorular_frame, columns=("Ders Adı", "Soru"), show="headings")
        tree.heading("Ders Adı", text="Ders Adı")
        tree.heading("Soru", text="Soru")

        for ders, sorular in self.sorular.items():
            for soru in sorular:
                tree.insert("", tk.END, values=(ders, soru))

        tree.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    uygulama = EgitimPlatformu(root)
    root.mainloop()
