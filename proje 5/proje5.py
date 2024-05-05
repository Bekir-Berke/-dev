import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QComboBox, QMessageBox, QHBoxLayout, QFormLayout, QListWidget, QDialog, QTextEdit
from PyQt5.QtGui import QIcon

class Egitmen:
    def __init__(self, isim, uzmanlik_alani):
        self.isim = isim
        self.uzmanlik_alani = uzmanlik_alani

class Ogrenci:
    def __init__(self, isim, email):
        self.isim = isim
        self.email = email

class Kurs:
    def __init__(self, kurs_adi, egitmen, icerik=None):
        self.kurs_adi = kurs_adi
        self.egitmen = egitmen
        self.icerik = icerik if icerik is not None else []
        self.ogrenciler = []

    def kaydol(self, ogrenci):
        if ogrenci not in self.ogrenciler:
            self.ogrenciler.append(ogrenci)
            return f"{ogrenci.isim} başarıyla {self.kurs_adi} kursuna kaydoldu."
        else:
            return f"{ogrenci.isim} zaten bu kursa kayıtlı."

class EgitimPlatformu:
    def __init__(self):
        self.kurslar = []
        self.egitmenler = []
        self.ogrenciler = []

    def kurs_ekle(self, kurs):
        self.kurslar.append(kurs)

    def egitmen_ekle(self, egitmen):
        self.egitmenler.append(egitmen)

    def ogrenci_ekle(self, ogrenci):
        self.ogrenciler.append(ogrenci)

class BilgiDialog(QDialog):
    def __init__(self, platform):
        super().__init__()
        self.platform = platform
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Kayıtlı Bilgiler")
        self.setGeometry(100, 100, 400, 600)
        self.setWindowIcon(QIcon('eğitim.png'))
        layout = QVBoxLayout()
        
        self.bilgi_edit = QTextEdit()
        self.bilgi_edit.setReadOnly(True)
        layout.addWidget(self.bilgi_edit)
        
        self.setLayout(layout)
        self.doldur_bilgiler()
    
    def doldur_bilgiler(self):
        bilgiler = ""
        for kurs in self.platform.kurslar:
            for ogrenci in kurs.ogrenciler:
                bilgiler += f"Öğrenci: {ogrenci.isim}, Kurs: {kurs.kurs_adi}, Eğitmen: {kurs.egitmen.isim}\n"
        self.bilgi_edit.setText(bilgiler)

class EgitimPlatformuGUI(QMainWindow):
    def __init__(self, platform):
        super().__init__()
        self.setWindowIcon(QIcon('eğitim.png'))

        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
                color: #333333;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QLineEdit, QTextEdit {
                border: 2px solid #4CAF50;
                padding: 5px;
            }
            QLabel {
                font-size: 16px;
            }
        """)

        self.platform = platform
        self.initUI()
        self.verileri_yukle()

    def verileri_yukle(self):
        try:
            with open("kayitli_ogrenciler.txt", "r") as file:
                for line in file:
                    isim, email, kurs_adi, egitmen_isim = line.strip().split(", ")
                    ogrenci = Ogrenci(isim, email)
                    if ogrenci not in self.platform.ogrenciler:
                        self.platform.ogrenci_ekle(ogrenci)
                    egitmen = next((e for e in self.platform.egitmenler if e.isim == egitmen_isim), None)
                    kurs = next((k for k in self.platform.kurslar if k.kurs_adi == kurs_adi and k.egitmen == egitmen), None)
                    if kurs and ogrenci not in kurs.ogrenciler:
                        kurs.kaydol(ogrenci)
        except FileNotFoundError:
            print("Dosya bulunamadı, yeni bir dosya oluşturulacak.")

    def initUI(self):
        self.setWindowTitle('Eğitim Platformu')
        self.setGeometry(100, 100, 500, 700)

        layout = QVBoxLayout()
        form_layout = QFormLayout()

        self.ogrenci_isim_input = QLineEdit()
        form_layout.addRow(QLabel("Öğrenci İsmi:"), self.ogrenci_isim_input)

        self.ogrenci_email_input = QLineEdit()
        form_layout.addRow(QLabel("Öğrenci E-Posta:"), self.ogrenci_email_input)

        self.ogrenci_ekle_button = QPushButton('Öğrenci Ekle')
        self.ogrenci_ekle_button.clicked.connect(self.ogrenci_ekle)
        form_layout.addRow(self.ogrenci_ekle_button)

        layout.addLayout(form_layout)

        self.ogrenci_listesi = QListWidget()
        layout.addWidget(self.ogrenci_listesi)

        self.kurs_secici = QComboBox()
        self.kurs_secici.addItems([kurs.kurs_adi for kurs in self.platform.kurslar])
        self.kurs_secici.currentIndexChanged.connect(self.update_egitmen_secici)
        layout.addWidget(self.kurs_secici)

        self.egitmen_secici = QComboBox()
        layout.addWidget(self.egitmen_secici)

        self.ogrenci_secici = QComboBox()
        layout.addWidget(self.ogrenci_secici)

        self.kaydol_button = QPushButton('Kursa Kaydol')
        self.kaydol_button.clicked.connect(self.kaydol)
        layout.addWidget(self.kaydol_button)

        self.bilgi_goster_button = QPushButton('Tüm Bilgileri Göster')
        self.bilgi_goster_button.clicked.connect(self.bilgileri_goster)
        layout.addWidget(self.bilgi_goster_button)

        self.kayitli_ogrenci_listesi = QListWidget()
        layout.addWidget(self.kayitli_ogrenci_listesi)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def ogrenci_ekle(self):
        isim = self.ogrenci_isim_input.text().strip()
        if not isim:
            QMessageBox.warning(self, 'Hata', 'Öğrenci ismi boş bırakılamaz.')
            return
        email = self.ogrenci_email_input.text()
        yeni_ogrenci = Ogrenci(isim, email)
        self.platform.ogrenci_ekle(yeni_ogrenci)
        self.ogrenci_listesi.addItem(f"{isim} ({email})")
        self.ogrenci_secici.addItem(f"{isim} ({email})")
        QMessageBox.information(self, 'Öğrenci Eklendi', f'"{isim}" başarıyla sisteme eklendi.')
        self.ogrenci_isim_input.clear()
        self.ogrenci_email_input.clear()

    def kaydol(self):
        secili_kurs_index = self.kurs_secici.currentIndex()
        secili_ogrenci_index = self.ogrenci_secici.currentIndex()
        if secili_ogrenci_index == -1 or secili_kurs_index == -1:
            QMessageBox.warning(self, 'Hata', 'Öğrenci veya kurs seçimi yapılmamış.')
            return
        secili_ogrenci = self.platform.ogrenciler[secili_ogrenci_index]
        secili_kurs = self.platform.kurslar[secili_kurs_index]
        secili_egitmen = secili_kurs.egitmen
        mesaj = secili_kurs.kaydol(secili_ogrenci)
        QMessageBox.information(self, 'Kayıt Bilgisi', mesaj)
        self.kayitli_ogrenci_listesi.addItem(f"{secili_ogrenci.isim} - {secili_egitmen.isim} - {secili_kurs.kurs_adi}")

    def update_egitmen_secici(self):
        self.egitmen_secici.clear()
        if self.kurs_secici.currentIndex() >= 0:
            secili_kurs = self.platform.kurslar[self.kurs_secici.currentIndex()]
            self.egitmen_secici.addItem(secili_kurs.egitmen.isim)

    def bilgileri_goster(self):
        dialog = BilgiDialog(self.platform)
        dialog.exec_()

    def closeEvent(self, event):
        with open("kayitli_ogrenciler.txt", "w") as file:
            for kurs in self.platform.kurslar:
                for ogrenci in kurs.ogrenciler:
                    file.write(f"{ogrenci.isim}, {ogrenci.email}, {kurs.kurs_adi}, {kurs.egitmen.isim}\n")
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    platform = EgitimPlatformu()


    egitmenler = [
        Egitmen("Ahmet Hoca", "Bilgisayar Bilimi"),
        Egitmen("Mehmet Hoca", "Veri Bilimi"),
        Egitmen("Elif Hoca", "Matematik"),
        Egitmen("Ayşe Hoca", "Fizik"),
        Egitmen("Fatma Hoca", "Kimya"),
        Egitmen("Ali Hoca", "Biyoloji"),
        Egitmen("Zeynep Hoca", "Tarih"),
        Egitmen("Emre Hoca", "Edebiyat")
    ]

    for egitmen in egitmenler:
        platform.egitmen_ekle(egitmen)

    kurslar = [
        Kurs("Programlama Temelleri", egitmenler[0]),
        Kurs("Veri Bilimi Giriş", egitmenler[1]),
        Kurs("Matematiksel Analiz", egitmenler[2]),
        Kurs("Fizik", egitmenler[3]),
        Kurs("Kimya", egitmenler[4]),
        Kurs("Biyoloji", egitmenler[5]),
        Kurs("Tarih Yolculuğu", egitmenler[6]),
        Kurs("Edebiyat", egitmenler[7])
    ]

    for kurs in kurslar:
        platform.kurs_ekle(kurs)

    ex = EgitimPlatformuGUI(platform)
    ex.show()
    sys.exit(app.exec_())