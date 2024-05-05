import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QComboBox, QMessageBox, QDialog

class Musteri:
    def __init__(self, isim, email):
        self.isim = isim
        self.email = email

class Satis:
    def __init__(self, urun_adi, musteri, miktar):
        self.urun_adi = urun_adi
        self.musteri = musteri
        self.miktar = miktar

class DestekTalebi:
    def __init__(self, musteri, konu, aciklama):
        self.musteri = musteri
        self.konu = konu
        self.aciklama = aciklama

class SirketPlatformu:
    def __init__(self):
        self.musteriler = []
        self.satislar = []
        self.destek_talepleri = []
        self.verileri_yukle()

    def musteri_ekle(self, musteri):
        self.musteriler.append(musteri)

    def satis_ekle(self, satis):
        self.satislar.append(satis)

    def destek_talebi_olustur(self, talep):
        self.destek_talepleri.append(talep)

    def verileri_kaydet(self):
        with open("veriler.json", "w") as file:
            json.dump({
                "musteriler": [(musteri.isim, musteri.email) for musteri in self.musteriler],
                "satislar": [(satis.urun_adi, satis.musteri.isim, satis.miktar) for satis in self.satislar],
                "destek_talepleri": [(talep.musteri.isim, talep.konu, talep.aciklama) for talep in self.destek_talepleri]
            }, file)

    def verileri_yukle(self):
        try:
            with open("veriler.json", "r") as file:
                veriler = json.load(file)
                self.musteriler = [Musteri(isim, email) for isim, email in veriler["musteriler"]]
                self.satislar = [Satis(urun_adi, Musteri(musteri_isim, ""), miktar) for urun_adi, musteri_isim, miktar in veriler["satislar"]]
                self.destek_talepleri = [DestekTalebi(Musteri(musteri_isim, ""), konu, aciklama) for musteri_isim, konu, aciklama in veriler["destek_talepleri"]]
        except FileNotFoundError:
            pass

class GirisPenceresi(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Giriş')
        layout = QVBoxLayout()
        self.ad_input = QLineEdit()
        self.ad_input.setPlaceholderText('Kullanıcı Adı')
        layout.addWidget(self.ad_input)
        self.sifre_input = QLineEdit()
        self.sifre_input.setPlaceholderText('Şifre')
        self.sifre_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.sifre_input)
        self.giris_button = QPushButton('Giriş')
        self.giris_button.clicked.connect(self.giris_kontrol)
        layout.addWidget(self.giris_button)
        self.setLayout(layout)

    def giris_kontrol(self):
        ad = self.ad_input.text()
        sifre = self.sifre_input.text()
        if ad == 'admin' and sifre == 'admin':
            self.accept()
        else:
            QMessageBox.warning(self, 'Hata', 'Geçersiz kullanıcı adı veya şifre.')

class SirketPlatformuGUI(QMainWindow):
    def __init__(self, platform):
        super().__init__()
        self.platform = platform
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Şirket Platformu')
        self.setGeometry(100, 100, 500, 700)
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

        layout = QVBoxLayout()

        self.musteri_isim_input = QLineEdit()
        layout.addWidget(QLabel("Müşteri İsmi:"))
        layout.addWidget(self.musteri_isim_input)

        self.musteri_email_input = QLineEdit()
        layout.addWidget(QLabel("Müşteri E-Posta:"))
        layout.addWidget(self.musteri_email_input)

        self.musteri_ekle_button = QPushButton('Müşteri Ekle')
        self.musteri_ekle_button.clicked.connect(self.musteri_ekle)
        layout.addWidget(self.musteri_ekle_button)

        self.musteri_combobox = QComboBox()
        layout.addWidget(QLabel("Müşteri Seç:"))
        layout.addWidget(self.musteri_combobox)

        self.musteri_listesini_guncelle()

        self.urun_input = QLineEdit()
        layout.addWidget(QLabel("Ürün ID:"))
        layout.addWidget(self.urun_input)

        self.miktar_input = QLineEdit()
        layout.addWidget(QLabel("Miktar:"))
        layout.addWidget(self.miktar_input)

        self.satis_ekle_button = QPushButton('Satış Yap')
        self.satis_ekle_button.clicked.connect(self.satis_ekle)
        layout.addWidget(self.satis_ekle_button)

        self.destek_konu_input = QLineEdit()
        layout.addWidget(QLabel("Konu:"))
        layout.addWidget(self.destek_konu_input)

        self.destek_aciklama_input = QLineEdit()
        layout.addWidget(QLabel("Açıklama:"))
        layout.addWidget(self.destek_aciklama_input)

        self.destek_talebi_olustur_button = QPushButton('Destek Talebi Oluştur')
        self.destek_talebi_olustur_button.clicked.connect(self.destek_talebi_olustur)
        layout.addWidget(self.destek_talebi_olustur_button)

        self.verileri_goruntule_button = QPushButton('Verileri Görüntüle')
        self.verileri_goruntule_button.clicked.connect(self.giris_ekrani)
        layout.addWidget(self.verileri_goruntule_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def musteri_ekle(self):
        isim = self.musteri_isim_input.text().strip()
        if not isim:
            QMessageBox.warning(self, 'Hata', 'Müşteri ismi boş bırakılamaz.')
            return
        email = self.musteri_email_input.text()
        yeni_musteri = Musteri(isim, email)
        self.platform.musteri_ekle(yeni_musteri)
        self.musteri_listesini_guncelle()
        QMessageBox.information(self, 'Müşteri Eklendi', f'"{isim}" başarıyla sisteme eklendi.')
        self.musteri_isim_input.clear()
        self.musteri_email_input.clear()

    def musteri_listesini_guncelle(self):
        self.musteri_combobox.clear()
        for musteri in self.platform.musteriler:
            self.musteri_combobox.addItem(f"{musteri.isim} ({musteri.email})")

    def satis_ekle(self):
        urun_adi = self.urun_input.text().strip()
        miktar = self.miktar_input.text().strip()
        if not urun_adi or not miktar:
            QMessageBox.warning(self, 'Hata', 'Ürün adı ve miktar boş bırakılamaz.')
            return
        try:
            miktar = int(miktar)
        except ValueError:
            QMessageBox.warning(self, 'Hata', 'Geçersiz miktar.')
            return
        if self.musteri_combobox.currentIndex() == -1:
            QMessageBox.warning(self, 'Hata', 'Satış yapabilmek için bir müşteri seçmelisiniz.')
            return
        musteri = self.platform.musteriler[self.musteri_combobox.currentIndex()]
        yeni_satis = Satis(urun_adi, musteri, miktar)
        self.platform.satis_ekle(yeni_satis)
        QMessageBox.information(self, 'Satış Yapıldı', f"{miktar} adet {urun_adi} satışı yapıldı.")
        self.urun_input.clear()
        self.miktar_input.clear()

    def destek_talebi_olustur(self):
        konu = self.destek_konu_input.text().strip()
        aciklama = self.destek_aciklama_input.text().strip()
        if not konu or not aciklama:
            QMessageBox.warning(self, 'Hata', 'Konu ve açıklama boş bırakılamaz.')
            return
        if self.musteri_combobox.currentIndex() == -1:
            QMessageBox.warning(self, 'Hata', 'Destek talebi oluşturabilmek için bir müşteri seçmelisiniz.')
            return
        musteri = self.platform.musteriler[self.musteri_combobox.currentIndex()]
        yeni_talep = DestekTalebi(musteri, konu, aciklama)
        self.platform.destek_talebi_olustur(yeni_talep)
        QMessageBox.information(self, 'Talep Oluşturuldu', 'Destek talebiniz oluşturuldu.')
        self.destek_konu_input.clear()
        self.destek_aciklama_input.clear()

    def verileri_goruntule(self):
        musteriler_mesaj = 'Henüz müşteri eklenmemiş.' if not self.platform.musteriler else '\n'.join([f"{musteri.isim} - {musteri.email}" for musteri in self.platform.musteriler])
        satislar_mesaj = 'Henüz satış yapılmamış.' if not self.platform.satislar else '\n'.join([f"{satis.musteri.isim}: {satis.urun_adi} - {satis.miktar} adet" for satis in self.platform.satislar])
        destek_talepleri_mesaj = 'Henüz destek talebi oluşturulmamış.' if not self.platform.destek_talepleri else '\n'.join([f"{talep.musteri.isim}: {talep.konu} - {talep.aciklama}" for talep in self.platform.destek_talepleri])

        QMessageBox.information(self, 'Veriler', f"Müşteriler:\n{musteriler_mesaj}\n\nSatışlar:\n{satislar_mesaj}\n\nDestek Talepleri:\n{destek_talepleri_mesaj}")

    def giris_ekrani(self):
        giris_penceresi = GirisPenceresi()
        if giris_penceresi.exec_() == QDialog.Accepted:
            self.verileri_goruntule()

    def closeEvent(self, event):
        self.platform.verileri_kaydet()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    platform = SirketPlatformu()

    ex = SirketPlatformuGUI(platform)
    ex.show()
    sys.exit(app.exec_())
