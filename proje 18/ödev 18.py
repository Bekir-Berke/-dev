import tkinter as tk
from tkinter import ttk

class Veritabani:
    def __init__(self):
        self.olaylar = []

    def olay_ekle(self, olay):
        self.olaylar.append(olay)

    def olay_sorgula(self, olay_adi):
        for olay in self.olaylar:
            if olay["adi"] == olay_adi:
                return olay
        return None

class Event:
    def __init__(self, adi, tarih, aciklama, sahsiyetler, donem):
        self.adi = adi
        self.tarih = tarih
        self.aciklama = aciklama
        self.sahsiyetler = sahsiyetler
        self.donem = donem

def olay_ekle():
    olay_adi = olay_adi_entry.get()
    olay_tarih = olay_tarih_entry.get()
    olay_aciklama = olay_aciklama_entry.get()
    sahsiyetler = sahsiyetler_entry.get().split(', ')
    donem = donem_entry.get()
    if olay_adi and olay_tarih and olay_aciklama and sahsiyetler and donem:
        olay = {"adi": olay_adi, "tarih": olay_tarih, "aciklama": olay_aciklama, "sahsiyetler": sahsiyetler, "donem": donem}
        veritabani.olay_ekle(olay)
        olay_ekle_durum.config(text="Olay başarıyla eklendi.", fg="green")
        listele_olaylar()
    else:
        olay_ekle_durum.config(text="Lütfen tüm alanları doldurun.", fg="red")

def listele_olaylar():
    tree.delete(*tree.get_children())
    for olay in veritabani.olaylar:
        tree.insert('', 'end', values=(olay["adi"], olay["tarih"], olay["aciklama"], ', '.join(olay["sahsiyetler"]), olay["donem"]))

def sorgula():
    olay_adi = sorgula_entry.get()
    olay = veritabani.olay_sorgula(olay_adi)
    if olay:
        sorgula_durum.config(text="")
        sorgu_pencere = tk.Toplevel(root)
        sorgu_pencere.title("Sorgulanan Olay")
        sorgu_pencere.geometry("400x200")
        
        tree_sorgu = ttk.Treeview(sorgu_pencere, columns=('Olay Adı', 'Tarih', 'Açıklama', 'Şahsiyetler', 'Dönem'), show='headings')
        tree_sorgu.pack(fill=tk.BOTH, expand=True)
        for col in ('Olay Adı', 'Tarih', 'Açıklama', 'Şahsiyetler', 'Dönem'):
            tree_sorgu.heading(col, text=col)
        tree_sorgu.insert('', 'end', values=(olay["adi"], olay["tarih"], olay["aciklama"], ', '.join(olay["sahsiyetler"]), olay["donem"]))
    else:
        sorgula_durum.config(text="Olay bulunamadı.", fg="red")
        listele_olaylar()

veritabani = Veritabani()

root = tk.Tk()
root.title("Veritabanı Yönetim Sistemi")
root.geometry("800x500")

main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill=tk.BOTH, expand=True)

# Olay Ekle
olay_ekle_frame = ttk.LabelFrame(main_frame, text="Olay Ekle", padding="20")
olay_ekle_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

tk.Label(olay_ekle_frame, text="Olay Adı:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
olay_adi_entry = tk.Entry(olay_ekle_frame, font=('Arial', 12))
olay_adi_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

tk.Label(olay_ekle_frame, text="Olay Tarihi:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
olay_tarih_entry = tk.Entry(olay_ekle_frame, font=('Arial', 12))
olay_tarih_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

tk.Label(olay_ekle_frame, text="Olay Açıklaması:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
olay_aciklama_entry = tk.Entry(olay_ekle_frame, font=('Arial', 12))
olay_aciklama_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

tk.Label(olay_ekle_frame, text="Şahsiyet:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
sahsiyetler_entry = tk.Entry(olay_ekle_frame, font=('Arial', 12))
sahsiyetler_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

tk.Label(olay_ekle_frame, text="Olayın Yaşandığı Dönem:").grid(row=4, column=0, padx=10, pady=10, sticky="e")
donem_entry = tk.Entry(olay_ekle_frame, font=('Arial', 12))
donem_entry.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

tk.Button(olay_ekle_frame, text="Olay Ekle", command=olay_ekle).grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

olay_ekle_durum = tk.Label(olay_ekle_frame, text="", fg="green", font=('Arial', 12))
olay_ekle_durum.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Sorgula
sorgula_frame = ttk.LabelFrame(main_frame, text="Olay Sorgula", padding="20")
sorgula_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

tk.Label(sorgula_frame, text="Sorgulanacak Olay Adı:", font=('Arial', 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
sorgula_entry = tk.Entry(sorgula_frame, font=('Arial', 12))
sorgula_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

tk.Button(sorgula_frame, text="Sorgula", command=sorgula).grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

sorgula_durum = tk.Label(sorgula_frame, text="", fg="red", font=('Arial', 12))
sorgula_durum.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Olaylar Treeview
tree_frame = ttk.Frame(main_frame)
tree_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

tree = ttk.Treeview(tree_frame, columns=('Olay Adı', 'Tarih', 'Açıklama', 'Şahsiyetler', 'Dönem'), show='headings')
tree.pack(fill=tk.BOTH, expand=True)
for col in ('Olay Adı', 'Tarih', 'Açıklama', 'Şahsiyetler', 'Dönem'):
    tree.heading(col, text=col)

# Örnek olayları bir liste olarak ekleyelim
daha_fazla_olaylar = [
    {"adi": "Berlin Duvarı'nın Yıkılışı", "tarih": "9 Kasım 1989", "aciklama": "Almanya'nın birleşmesinin önünü açan olay.", "sahsiyetler": ["Mikhail Gorbachev"], "donem": "20. yüzyıl"},
    {"adi": "Apollo 11'in Ay'a İnişi", "tarih": "20 Temmuz 1969", "aciklama": "İlk insanlı Ay inişi.", "sahsiyetler": ["Neil Armstrong", "Buzz Aldrin"], "donem": "20. yüzyıl"},
    {"adi": "Çanakkale Savaşı", "tarih": "18 Mart - 24 Nisan 1915", "aciklama": "Osmanlı İmparatorluğu'nun İtilaf Devletleri'ne karşı kazandığı büyük zafer.", "sahsiyetler": ["Mustafa Kemal Atatürk", "Winston Churchill"], "donem": "20. yüzyıl"},
    {"adi": "Birinci Meşrutiyetin İlanı", "tarih": "23 Temmuz 1876", "aciklama": "Osmanlı İmparatorluğu'nda anayasal monarşinin ilan edildiği gün.", "sahsiyetler": ["II. Abdülhamid"], "donem": "19. yüzyıl"},
    {"adi": "Amerika'nın Keşfi", "tarih": "12 Ekim 1492", "aciklama": "Kristof Kolomb'un Amerika kıtasını keşfi.", "sahsiyetler": ["Kristof Kolomb"], "donem": "15. yüzyıl"},
    {"adi": "Rönesans Dönemi", "tarih": "14. yüzyıl - 17. yüzyıl", "aciklama": "Avrupa'da sanat, bilim ve kültürde büyük değişim ve yeniliklerin yaşandığı dönem.", "sahsiyetler": ["Leonardo da Vinci", "Michelangelo"], "donem": "14. yüzyıl - 17. yüzyıl"},
    {"adi": "Bilgi Çağı Başlangıcı", "tarih": "20. yüzyıl", "aciklama": "Bilgisayar ve iletişim teknolojilerindeki hızlı gelişmelerin yaşandığı dönem.", "sahsiyetler": ["Bill Gates", "Steve Jobs"], "donem": "20. yüzyıl"},
    {"adi": "Hindistan'ın Bağımsızlık Mücadelesi", "tarih": "20. yüzyıl", "aciklama": "Hindistan'ın Britanya sömürgeciliğine karşı verdiği mücadele.", "sahsiyetler": ["Mahatma Gandhi", "Jawaharlal Nehru"], "donem": "20. yüzyıl"},
    {"adi": "Reformasyon", "tarih": "16. yüzyıl", "aciklama": "Hristiyanlık'ta dini reform hareketleri ve Katolik Kilisesi'nin bölünmesi.", "sahsiyetler": ["Martin Luther", "John Calvin"], "donem": "16. yüzyıl"},
    {"adi": "Fransız İhtilali", "tarih": "14 Temmuz 1789", "aciklama": "Fransa'da monarşinin devrilmesi ve cumhuriyetin ilan edilmesi.", "sahsiyetler": ["Napolyon Bonapart", "Marie Antoinette"], "donem": "18. yüzyıl"},
]

# Örnek olayları veritabanına ekleyelim
for olay in daha_fazla_olaylar:
    veritabani.olay_ekle(olay)
    
# Olayları listele
listele_olaylar()

root.mainloop()
