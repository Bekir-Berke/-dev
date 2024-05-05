import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class Kullanici:
    def __init__(self, id, ad, soyad, email):
        self.id = id
        self.ad = ad
        self.soyad = soyad
        self.email = email

    def __str__(self):
        return f"ID: {self.id}, {self.ad} {self.soyad} - {self.email}"

class Etkinlik:
    def __init__(self, adi, tarih, mekan):
        self.adi = adi
        self.tarih = tarih
        self.mekan = mekan

    def __str__(self):
        return f"{self.adi} - {self.tarih} - {self.mekan}"

class Bilet:
    def __init__(self, id, numara, etkinlik):
        self.id = id
        self.numara = numara
        self.etkinlik = etkinlik

    def __str__(self):
        return f"ID: {self.id}, Bilet No: {self.numara}, Etkinlik: {self.etkinlik.adi}"

class KullaniciEklePencere(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kullanıcı Ekle")
        self.setGeometry(300, 300, 400, 200)

        layout = QVBoxLayout()

        id_label = QLabel("ID:")
        self.id_input = QLineEdit()

        ad_label = QLabel("Ad:")
        self.ad_input = QLineEdit()

        soyad_label = QLabel("Soyad:")
        self.soyad_input = QLineEdit()

        email_label = QLabel("E-mail:")
        self.email_input = QLineEdit()

        ekle_button = QPushButton("Kullanıcı Ekle")
        ekle_button.clicked.connect(self.ekle_kullanici)

        layout.addWidget(id_label)
        layout.addWidget(self.id_input)
        layout.addWidget(ad_label)
        layout.addWidget(self.ad_input)
        layout.addWidget(soyad_label)
        layout.addWidget(self.soyad_input)
        layout.addWidget(email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(ekle_button)

        self.setLayout(layout)

    def ekle_kullanici(self):
        id = self.id_input.text()
        ad = self.ad_input.text()
        soyad = self.soyad_input.text()
        email = self.email_input.text()

        if id and ad and soyad and email:
            kullanici = Kullanici(id, ad, soyad, email)
            QMessageBox.information(self, "Bilgi", f"{ad} {soyad} kullanıcı eklendi.")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun.")

class EtkinlikEklePencere(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Etkinlik Ekle")
        self.setGeometry(300, 300, 400, 200)

        layout = QVBoxLayout()

        etkinlik_adi_label = QLabel("Etkinlik Adı:")
        self.etkinlik_adi_input = QLineEdit()

        tarih_label = QLabel("Tarih:")
        self.tarih_input = QLineEdit()

        mekan_label = QLabel("Mekan:")
        self.mekan_input = QLineEdit()

        ekle_button = QPushButton("Etkinlik Ekle")
        ekle_button.clicked.connect(self.ekle_etkinlik)

        layout.addWidget(etkinlik_adi_label)
        layout.addWidget(self.etkinlik_adi_input)
        layout.addWidget(tarih_label)
        layout.addWidget(self.tarih_input)
        layout.addWidget(mekan_label)
        layout.addWidget(self.mekan_input)
        layout.addWidget(ekle_button)

        self.setLayout(layout)

    def ekle_etkinlik(self):
        adi = self.etkinlik_adi_input.text()
        tarih = self.tarih_input.text()
        mekan = self.mekan_input.text()

        if adi and tarih and mekan:
            etkinlik = Etkinlik(adi, tarih, mekan)
            QMessageBox.information(self, "Bilgi", f"{adi} etkinliği eklendi.")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun.")

class BiletAlPencere(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bilet Al")
        self.setGeometry(300, 300, 400, 200)

        layout = QVBoxLayout()

        id_label = QLabel("ID:")
        self.id_input = QLineEdit()

        bilet_numarasi_label = QLabel("Bilet Numarası:")
        self.bilet_numarasi_input = QLineEdit()

        etkinlik_adi_label = QLabel("Etkinlik Adı:")
        self.etkinlik_adi_input = QLineEdit()

        al_button = QPushButton("Bilet Al")
        al_button.clicked.connect(self.al_bilet)

        layout.addWidget(id_label)
        layout.addWidget(self.id_input)
        layout.addWidget(bilet_numarasi_label)
        layout.addWidget(self.bilet_numarasi_input)
        layout.addWidget(etkinlik_adi_label)
        layout.addWidget(self.etkinlik_adi_input)
        layout.addWidget(al_button)

        self.setLayout(layout)

    def al_bilet(self):
        id = self.id_input.text()
        numara = self.bilet_numarasi_input.text()
        etkinlik_adi = self.etkinlik_adi_input.text()

        if id and numara and etkinlik_adi:
            bilet = Bilet(id, numara, Etkinlik(etkinlik_adi, "", ""))
            QMessageBox.information(self, "Bilgi", f"{numara} numaralı bilet satın alındı.")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun.")

class BiletSatPencere(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bilet Sat")
        self.setGeometry(300, 300, 400, 200)

        layout = QVBoxLayout()

        id_label = QLabel("ID:")
        self.id_input = QLineEdit()

        bilet_numarasi_label = QLabel("Bilet Numarası:")
        self.bilet_numarasi_input = QLineEdit()

        etkinlik_adi_label = QLabel("Etkinlik Adı:")
        self.etkinlik_adi_input = QLineEdit()

        sat_button = QPushButton("Bilet Sat")
        sat_button.clicked.connect(self.sat_bilet)

        layout.addWidget(id_label)
        layout.addWidget(self.id_input)
        layout.addWidget(bilet_numarasi_label)
        layout.addWidget(self.bilet_numarasi_input)
        layout.addWidget(etkinlik_adi_label)
        layout.addWidget(self.etkinlik_adi_input)
        layout.addWidget(sat_button)

        self.setLayout(layout)

    def sat_bilet(self):
        id = self.id_input.text()
        numara = self.bilet_numarasi_input.text()
        etkinlik_adi = self.etkinlik_adi_input.text()

        if id and numara and etkinlik_adi:
            QMessageBox.information(self, "Bilgi", f"{numara} numaralı bilet satıldı.")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun.")

class Arayuz(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Etkinlik ve Bilet Satış Platformu")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        kullanici_ekle_button = QPushButton("Kullanıcı Ekle")
        kullanici_ekle_button.clicked.connect(self.ac_kullanici_ekle)

        etkinlik_ekle_button = QPushButton("Etkinlik Ekle")
        etkinlik_ekle_button.clicked.connect(self.ac_etkinlik_ekle)

        bilet_al_button = QPushButton("Bilet Al")
        bilet_al_button.clicked.connect(self.ac_bilet_al)

        bilet_sat_button = QPushButton("Bilet Sat")
        bilet_sat_button.clicked.connect(self.ac_bilet_sat)

        self.layout.addWidget(kullanici_ekle_button)
        self.layout.addWidget(etkinlik_ekle_button)
        self.layout.addWidget(bilet_al_button)
        self.layout.addWidget(bilet_sat_button)

        self.central_widget.setLayout(self.layout)

    def ac_kullanici_ekle(self):
        self.kullanici_ekle_pencere = KullaniciEklePencere()
        self.kullanici_ekle_pencere.show()

    def ac_etkinlik_ekle(self):
        self.etkinlik_ekle_pencere = EtkinlikEklePencere()
        self.etkinlik_ekle_pencere.show()

    def ac_bilet_al(self):
        self.bilet_al_pencere = BiletAlPencere()
        self.bilet_al_pencere.show()

    def ac_bilet_sat(self):
        self.bilet_sat_pencere = BiletSatPencere()
        self.bilet_sat_pencere.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    arayuz = Arayuz()
    arayuz.show()
    sys.exit(app.exec_())

