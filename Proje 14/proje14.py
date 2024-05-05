import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QCalendarWidget, QComboBox, QListWidget, QGroupBox, QFormLayout, QTextEdit
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt

class Proje:
    def __init__(self, adi, baslangic_tarihi, bitis_tarihi):
        self.adi = adi
        self.baslangic_tarihi = baslangic_tarihi
        self.bitis_tarihi = bitis_tarihi
        self.gorevler = []


    def gorev_ekle(self, gorev):
        self.gorevler.append(gorev)

    def gorev_ata(self, gorev_adi, sorumlu_kisi):
        for gorev in self.gorevler:
            if gorev.adi == gorev_adi:
                gorev.sorumlu_kisi = sorumlu_kisi
                break

    def ilerleme_kaydet(self, gorev_adi, ilerleme):
        for gorev in self.gorevler:
            if gorev.adi == gorev_adi:
                gorev.ilerleme = ilerleme
                break

    def gorevleri_listele(self):
        return self.gorevler

    def kaydet(self):
        with open(f"{self.adi}_gorevler.txt", "w") as file:
            for gorev in self.gorevler:
                file.write(f"Görev Adı: {gorev.adi}, Sorumlu Kişi: {gorev.sorumlu_kisi}, İlerleme: {gorev.ilerleme}\n")

class Gorev:
    def __init__(self, adi):
        self.adi = adi
        self.sorumlu_kisi = ""
        self.ilerleme = ""

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Proje Yönetim Sistemi")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #f0f0f0; color: #333; font-family: Arial;")
        self.setWindowIcon(QIcon("icon.png"))
        self.label_adi = QLabel("Proje Adı:")
        self.label_adi.setFont(QFont("Arial", 12, QFont.Bold))
        self.input_adi = QLineEdit()
        self.label_baslangic = QLabel("Başlangıç Tarihi:")
        self.label_baslangic.setFont(QFont("Arial", 12, QFont.Bold))
        self.calendar_baslangic = QCalendarWidget()
        self.label_bitis = QLabel("Bitiş Tarihi:")
        self.label_bitis.setFont(QFont("Arial", 12, QFont.Bold))
        self.calendar_bitis = QCalendarWidget()

        self.button_olustur = QPushButton("Proje Oluştur")
        self.button_olustur.setStyleSheet("background-color: #007bff; color: #fff; font-weight: bold;")
        self.button_olustur.clicked.connect(self.proje_olustur)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label_adi)
        self.layout.addWidget(self.input_adi)
        self.layout.addWidget(self.label_baslangic)
        self.layout.addWidget(self.calendar_baslangic)
        self.layout.addWidget(self.label_bitis)
        self.layout.addWidget(self.calendar_bitis)
        self.layout.addWidget(self.button_olustur)

        self.proje_groupbox = QGroupBox("Proje Detayları")
        self.proje_groupbox.setStyleSheet("QGroupBox { background-color: #fff; border: 2px solid #007bff; border-radius: 10px; }")
        self.proje_layout = QFormLayout()
        self.proje_groupbox.setLayout(self.proje_layout)

        self.layout.addWidget(self.proje_groupbox)

        self.button_gorev_ekle = QPushButton("Görev Ekle")
        self.button_gorev_ekle.setStyleSheet("background-color: #28a745; color: #fff; font-weight: bold;")
        self.button_gorev_ekle.clicked.connect(self.gorev_ekle)
        self.layout.addWidget(self.button_gorev_ekle)

        self.gorev_listesi = QListWidget()
        self.gorev_listesi.itemClicked.connect(self.gorev_detay)
        self.layout.addWidget(self.gorev_listesi)

        self.setLayout(self.layout)

    def proje_olustur(self):
        proje_adi = self.input_adi.text()
        baslangic_tarihi = self.calendar_baslangic.selectedDate().toString("yyyy-MM-dd")
        bitis_tarihi = self.calendar_bitis.selectedDate().toString("yyyy-MM-dd")

        self.proje = Proje(proje_adi, baslangic_tarihi, bitis_tarihi)
        self.proje_layout.addRow(QLabel("Proje Adı:"), QLabel(self.proje.adi))
        self.proje_layout.addRow(QLabel("Başlangıç Tarihi:"), QLabel(self.proje.baslangic_tarihi))
        self.proje_layout.addRow(QLabel("Bitiş Tarihi:"), QLabel(self.proje.bitis_tarihi))

    def gorev_ekle(self):
        self.input_gorev_adi = QLineEdit()
        self.input_gorev_adi.setStyleSheet("background-color: #fff; color: #333;")
        self.label_gorev_adi = QLabel("Görev Adı:")
        self.label_gorev_adi.setFont(QFont("Arial", 10))
        self.proje_layout.addRow(self.label_gorev_adi, self.input_gorev_adi)

        self.combo_sorumlu = QComboBox()
        self.combo_sorumlu.addItems(["Arda", "Bekir", "Mehmet","Soner","İbrahim"])
        self.combo_sorumlu.setStyleSheet("background-color: #fff; color: #333;")
        self.label_sorumlu = QLabel("Sorumlu Kişi:")
        self.label_sorumlu.setFont(QFont("Arial", 10))
        self.proje_layout.addRow(self.label_sorumlu, self.combo_sorumlu)

        self.input_ilerleme = QTextEdit()
        self.input_ilerleme.setStyleSheet("background-color: #fff; color: #333;")
        self.label_ilerleme = QLabel("İlerleme Durumu:")
        self.label_ilerleme.setFont(QFont("Arial", 10))
        self.proje_layout.addRow(self.label_ilerleme, self.input_ilerleme)

        self.button_gorev_kaydet = QPushButton("Görev Kaydet")
        self.button_gorev_kaydet.setStyleSheet("background-color: #dc3545; color: #fff; font-weight: bold;")
        self.button_gorev_kaydet.clicked.connect(self.gorev_kaydet)
        self.proje_layout.addRow(self.button_gorev_kaydet)

    def gorev_kaydet(self):
        gorev_adi = self.input_gorev_adi.text()
        sorumlu_kisi = self.combo_sorumlu.currentText()
        ilerleme = self.input_ilerleme.toPlainText()

        gorev = Gorev(gorev_adi)
        gorev.sorumlu_kisi = sorumlu_kisi
        gorev.ilerleme = ilerleme

        self.proje.gorev_ekle(gorev)
        self.gorev_listesi.addItem(gorev.adi)
        QMessageBox.information(self, "Bildirim", "Görev Eklendi ve Atandı!")
        self.proje.kaydet()  # Görev ekledikten sonra veriyi kaydet

    def gorev_detay(self, item):
        for gorev in self.proje.gorevleri_listele():
            if item.text() == gorev.adi:
                QMessageBox.information(self, "Görev Detayları", f"Görev Adı: {gorev.adi}\nSorumlu Kişi: {gorev.sorumlu_kisi}\nİlerleme: {gorev.ilerleme}")
                break

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Giriş Yap")
        self.setGeometry(100, 100, 400, 200)
        self.setStyleSheet("background-color: #f0f0f0; color: #333; font-family: Arial;")
        self.setWindowIcon(QIcon("icon.png"))
        self.label_username = QLabel("Kullanıcı Adı:")
        self.label_username.setFont(QFont("Arial", 12, QFont.Bold))
        self.input_username = QLineEdit()
        self.label_password = QLabel("Şifre:")
        self.label_password.setFont(QFont("Arial", 12, QFont.Bold))
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)  # Şifrenin görüntülenmesini engeller

        self.button_login = QPushButton("Giriş Yap")
        self.button_login.setStyleSheet("background-color: #007bff; color: #fff; font-weight: bold;")
        self.button_login.clicked.connect(self.login)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label_username)
        self.layout.addWidget(self.input_username)
        self.layout.addWidget(self.label_password)
        self.layout.addWidget(self.input_password)
        self.layout.addWidget(self.button_login)

        self.setLayout(self.layout)

    def login(self):
        username = self.input_username.text()
        password = self.input_password.text()

        if username == "admin" and password == "12345":  # Örnek kullanıcı adı ve şifre
            self.main_window = MainWindow()  # Ana pencereyi oluştur
            self.main_window.show()
            self.close()  # Giriş penceresini kapat
        else:
            QMessageBox.warning(self, "Hata", "Kullanıcı adı veya şifre yanlış!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()  # Giriş penceresini oluştur
    login_window.show()
    sys.exit(app.exec_())
