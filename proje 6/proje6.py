import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QMessageBox, QTextEdit, QListWidget, QDialog, QVBoxLayout, QListWidgetItem
from PyQt5.QtGui import QIcon, QFont
class Tarif:
    def __init__(self, ad, malzemeler, icerik):
        self.ad = ad
        self.malzemeler = malzemeler
        self.icerik = icerik
        self.yorumlar = []

    def to_dict(self):
        return {
            'ad': self.ad,
            'malzemeler': self.malzemeler,
            'icerik': self.icerik
        }

class Kullanıcı:
    def __init__(self, kullanıcı_adı, şifre):
        self.kullanıcı_adı = kullanıcı_adı
        self.şifre = şifre

class TarifGosterDialog(QDialog):
    def __init__(self, tarifler, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Tarifler")
        self.setGeometry(300, 300, 800, 600)
        layout = QVBoxLayout(self)

        tarif_list_widget = QListWidget()
        for tarif in tarifler:
            tarif_ad_item = QListWidgetItem(tarif.ad)
            tarif_ad_item.setFont(QFont('Arial', 12, QFont.Bold))
            tarif_list_widget.addItem(tarif_ad_item)

            tarif_icerik_item = QListWidgetItem("   " + tarif.icerik)
            tarif_icerik_item.setFont(QFont('Arial', 10))
            tarif_list_widget.addItem(tarif_icerik_item)

        layout.addWidget(tarif_list_widget)
        self.setLayout(layout)

class YemekApp(QMainWindow):
    def __init__(self, tarif_data_file):
        super().__init__()

        self.setWindowIcon(QIcon('unnamed.png'))

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

        self.tarif_data_file = tarif_data_file
        self.tarifler = self.load_tarifler()

        self.setWindowTitle("Yemek Tarifi Uygulaması")
        self.setGeometry(200, 200, 500, 300)

        self.tarif_adı_label = QLabel('Tarif Adı:', self)
        self.tarif_adı_label.move(20, 20)

        self.btn_ekle = QPushButton('Tarif Ekle', self)
        self.btn_ekle.move(20, 220) 
        self.btn_ekle.resize(200, 40)
        self.btn_ekle.clicked.connect(self.tarif_ekle)

        self.tarif_adı_text = QLineEdit(self)
        self.tarif_adı_text.move(120, 20)
        self.tarif_adı_text.resize(200, 32)

        self.tarif_icerik_label = QLabel('Tarif İçeriği:', self)
        self.tarif_icerik_label.move(20, 60)

        self.tarif_icerik_text = QTextEdit(self)
        self.tarif_icerik_text.move(120, 60)
        self.tarif_icerik_text.resize(300, 150)

        self.btn_goster = QPushButton('Tarifleri Göster', self) 
        self.btn_goster.move(250, 220)
        self.btn_goster.resize(200, 40) 
        self.btn_goster.clicked.connect(self.tarifleri_goster)

        

    def tarif_ekle(self):
        tarif_adı = self.tarif_adı_text.text()
        tarif_icerik = self.tarif_icerik_text.toPlainText()
        yeni_tarif = Tarif(tarif_adı, [], tarif_icerik)
        self.tarifler.append(yeni_tarif)
        self.save_tarifler()
        QMessageBox.information(self, 'Tarif Eklendi', f'Tarif başarıyla eklendi: {tarif_adı}')
        self.tarif_adı_text.clear()
        self.tarif_icerik_text.clear()

    def tarifleri_goster(self):
        dialog = TarifGosterDialog(self.tarifler, self)
        dialog.exec_()

    def load_tarifler(self):
        try:
            with open(self.tarif_data_file, 'r') as file:
                tarif_dicts = json.load(file)
                return [Tarif(t['ad'], t.get('malzemeler', []), t['icerik']) for t in tarif_dicts]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tarifler(self):
        with open(self.tarif_data_file, 'w') as file:
            json.dump([t.to_dict() for t in self.tarifler], file)

class LoginWindow(QMainWindow):
    def __init__(self, user_data_file, tarif_data_file):
        super().__init__()

        self.setWindowIcon(QIcon('unnamed.png'))

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
        self.user_data_file = user_data_file
        self.kullanıcılar = self.load_users()

        self.setWindowTitle("Giriş Yap")
        self.setGeometry(200, 200, 300, 200)

        self.kullanıcı_adı_label = QLabel('Kullanıcı Adı:', self)
        self.kullanıcı_adı_label.move(20, 20)

        self.kullanıcı_adı_text = QLineEdit(self)
        self.kullanıcı_adı_text.move(120, 20)
        self.kullanıcı_adı_text.resize(150, 32)

        self.şifre_label = QLabel('Şifre:', self)
        self.şifre_label.move(20, 60)

        self.şifre_text = QLineEdit(self)
        self.şifre_text.setEchoMode(QLineEdit.Password)
        self.şifre_text.move(120, 60)
        self.şifre_text.resize(150, 32)

        self.login_button = QPushButton('Giriş Yap', self)
        self.login_button.move(20, 100)
        self.login_button.resize(100, 40)
        self.login_button.clicked.connect(self.check_credentials)

        self.register_button = QPushButton('Kayıt Ol', self)
        self.register_button.move(140, 100)
        self.register_button.resize(100, 40)
        self.register_button.clicked.connect(self.register_user)

    def check_credentials(self):
        user = self.kullanıcı_adı_text.text()
        password = self.şifre_text.text()
        if user in self.kullanıcılar and self.kullanıcılar[user] == password:
            self.tarif_ekranı = YemekApp('tarifler.json')
            self.tarif_ekranı.show()
            self.close()
        else:
            QMessageBox.warning(self, 'Hata', 'Yanlış kullanıcı adı veya şifre!')

    def register_user(self):
        user = self.kullanıcı_adı_text.text()
        password = self.şifre_text.text()
        if user and password:
            self.kullanıcılar[user] = password
            self.save_users()
            QMessageBox.information(self, 'Kayıt Başarılı', 'Kullanıcı başarıyla kaydedildi!')
        else:
            QMessageBox.warning(self, 'Hata', 'Kullanıcı adı ve şifre boş bırakılamaz!')

    def load_users(self):
        try:
            with open(self.user_data_file, 'r') as file:
                kullanıcılar = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            kullanıcılar = {}
        return kullanıcılar

    def save_users(self):
        with open(self.user_data_file, 'w') as file:
            json.dump(self.kullanıcılar, file)

def main():
    app = QApplication(sys.argv)
    login_window = LoginWindow('users.json', 'tarifler.json')
    login_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()