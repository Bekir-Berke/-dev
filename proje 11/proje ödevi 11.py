import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QComboBox, QDialog
from PyQt5.QtGui import QIcon 

class GirisPenceresi(QWidget):
    def __init__(self):
        super().__init__()
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
        self.setWindowTitle("Giriş")
        self.setGeometry(200, 200, 300, 150)

        self.kullanici_adi_etiketi = QLabel("Kullanıcı Adı:")
        self.kullanici_adi_girdisi = QLineEdit()
        self.sifre_etiketi = QLabel("Şifre:")
        self.sifre_girdisi = QLineEdit()
        self.sifre_girdisi.setEchoMode(QLineEdit.Password)
        self.giris_butonu = QPushButton("Giriş")
        self.giris_butonu.clicked.connect(self.giris)

        layout = QVBoxLayout()
        layout.addWidget(self.kullanici_adi_etiketi)
        layout.addWidget(self.kullanici_adi_girdisi)
        layout.addWidget(self.sifre_etiketi)
        layout.addWidget(self.sifre_girdisi)
        layout.addWidget(self.giris_butonu)

        self.setLayout(layout)

    def giris(self):
        kullanici_adi = self.kullanici_adi_girdisi.text()
        sifre = self.sifre_girdisi.text()

        if kullanici_adi == "admin" and sifre == "admin":
            self.close()
            self.anasayfa_penceresi = AnaSayfaPenceresi()
            self.anasayfa_penceresi.show()
        else:
            QMessageBox.warning(self, "Giriş Başarısız", "Geçersiz kullanıcı adı veya şifre")

class AnaSayfaPenceresi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enstrüman Dükkanı Yönetimi")
        self.setGeometry(200, 200, 500, 300)
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

        self.enstrumanlar = {
            "Gitar": {"stok": 10},
            "Piyano": {"stok": 10},
            "Keman": {"stok": 10},
            "Davul": {"stok": 10}
        }

        self.stok_label = QLabel("Stoklar:")
        self.stok_combo = QComboBox()
        self.stok_combo.addItems(self.enstrumanlar.keys())
        self.stok_combo.currentIndexChanged.connect(self.stok_miktarini_guncelle)

        self.stok_miktari_label = QLabel("Mevcut Stok Miktarı:")
        self.stok_miktari_goster = QLabel(str(self.enstrumanlar[self.stok_combo.currentText()]["stok"]))

        self.stok_artir_label = QLabel("Stok Miktarını Artır:")
        self.stok_artir_input = QLineEdit()

        self.stok_guncelle_butonu = QPushButton("Stok Güncelle")
        self.stok_guncelle_butonu.clicked.connect(self.stok_guncelle)

        self.satis_verileri_butonu = QPushButton("Satış Verilerini Görüntüle")
        self.satis_verileri_butonu.clicked.connect(self.satis_verilerini_goruntule)

        self.satis_yap_butonu = QPushButton("Satış Yap")
        self.satis_yap_butonu.clicked.connect(self.satis_yap_dialog)

        self.enstruman_ekle_butonu = QPushButton("Enstrüman Ekle")
        self.enstruman_ekle_butonu.clicked.connect(self.enstruman_ekle_dialog)

        layout = QVBoxLayout()
        layout.addWidget(self.stok_label)
        layout.addWidget(self.stok_combo)
        layout.addWidget(self.stok_miktari_label)
        layout.addWidget(self.stok_miktari_goster)
        layout.addWidget(self.stok_artir_label)
        layout.addWidget(self.stok_artir_input)
        layout.addWidget(self.stok_guncelle_butonu)
        layout.addWidget(self.satis_verileri_butonu)
        layout.addWidget(self.satis_yap_butonu)
        layout.addWidget(self.enstruman_ekle_butonu)

        self.setLayout(layout)

    def stok_guncelle(self):
        secilen_enstruman = self.stok_combo.currentText()
        artis_miktari = int(self.stok_artir_input.text())
        mevcut_stok = self.enstrumanlar[secilen_enstruman]["stok"]
        yeni_stok_miktari = mevcut_stok + artis_miktari
        self.enstrumanlar[secilen_enstruman]["stok"] = yeni_stok_miktari
        self.stok_miktari_goster.setText(str(yeni_stok_miktari))

    def stok_miktarini_guncelle(self):
        secilen_enstruman = self.stok_combo.currentText()
        mevcut_stok = self.enstrumanlar[secilen_enstruman]["stok"]
        self.stok_miktari_goster.setText(str(mevcut_stok))

    def satis_verilerini_goruntule(self):
        if not os.path.exists("satis_verileri.txt"):
            QMessageBox.information(self, "Satış Verileri", "Henüz satış verisi bulunmamaktadır.")
        else:
            with open("satis_verileri.txt", "r") as dosya:
                satilan_enstrumanlar = dosya.read()
                QMessageBox.information(self, "Satış Verileri", satilan_enstrumanlar)

    def satis_yap_dialog(self):
        dialog = SatisYapDialog(self.enstrumanlar, self)
        dialog.exec_()

    def enstruman_ekle_dialog(self):
        dialog = EnstrumanEkleDialog(self.enstrumanlar, self)
        dialog.exec_()

class SatisYapDialog(QDialog):
    def __init__(self, enstrumanlar, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Satış Yap")
        self.setGeometry(300, 300, 300, 200)
        self.enstrumanlar = enstrumanlar
        self.parent = parent

        self.enstruman_label = QLabel("Enstrüman:")
        self.enstruman_combo = QComboBox()
        self.enstruman_combo.addItems(self.enstrumanlar.keys())

        self.adet_label = QLabel("Adet:")
        self.adet_input = QLineEdit()

        self.fiyat_label = QLabel("Birim Fiyatı:")
        self.fiyat_input = QLineEdit()

        self.sat_button = QPushButton("Satış Yap")
        self.sat_button.clicked.connect(self.sat)

        layout = QVBoxLayout()
        layout.addWidget(self.enstruman_label)
        layout.addWidget(self.enstruman_combo)
        layout.addWidget(self.adet_label)
        layout.addWidget(self.adet_input)
        layout.addWidget(self.fiyat_label)
        layout.addWidget(self.fiyat_input)
        layout.addWidget(self.sat_button)

        self.setLayout(layout)

    def sat(self):
        enstruman = self.enstruman_combo.currentText()
        adet = int(self.adet_input.text())
        fiyat = float(self.fiyat_input.text())

        if adet > self.enstrumanlar[enstruman]["stok"]:
            QMessageBox.warning(self, "Yetersiz Stok", "Satış miktarı, stoktaki miktarı aşıyor!")
            return

        yeni_stok_miktari = self.enstrumanlar[enstruman]["stok"] - adet
        self.enstrumanlar[enstruman]["stok"] = yeni_stok_miktari
        self.parent.stok_miktari_goster.setText(str(yeni_stok_miktari))
        QMessageBox.information(self, "Satış Bilgisi", f"{enstruman} enstrümanından {adet} adet satış yapıldı.\nToplam fiyat: {fiyat * adet}")

class EnstrumanEkleDialog(QDialog):
    def __init__(self, enstrumanlar, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Enstrüman Ekle")
        self.setGeometry(300, 300, 300, 150)
        self.enstrumanlar = enstrumanlar
        self.parent = parent

        self.enstruman_ad_label = QLabel("Enstrüman Adı:")
        self.enstruman_ad_input = QLineEdit()

        self.stok_miktari_label = QLabel("Stok Miktarı:")
        self.stok_miktari_input = QLineEdit()

        self.ekle_button = QPushButton("Enstrüman Ekle")
        self.ekle_button.clicked.connect(self.enstruman_ekle)

        layout = QVBoxLayout()
        layout.addWidget(self.enstruman_ad_label)
        layout.addWidget(self.enstruman_ad_input)
        layout.addWidget(self.stok_miktari_label)
        layout.addWidget(self.stok_miktari_input)
        layout.addWidget(self.ekle_button)

        self.setLayout(layout)

    def enstruman_ekle(self):
        enstruman_ad = self.enstruman_ad_input.text()
        stok_miktari = int(self.stok_miktari_input.text())

        if enstruman_ad in self.enstrumanlar:
            QMessageBox.warning(self, "Enstrüman Zaten Var", "Bu enstrüman zaten mevcut!")
            return

        self.enstrumanlar[enstruman_ad] = {"stok": stok_miktari}
        self.parent.stok_combo.addItem(enstruman_ad)
        QMessageBox.information(self, "Enstrüman Eklendi", f"{enstruman_ad} enstrümanı başarıyla eklendi!")
        self.close()

if __name__ == "__main__":
    uygulama = QApplication(sys.argv)
    giris_penceresi = GirisPenceresi()
    giris_penceresi.show()
    sys.exit(uygulama.exec_())
