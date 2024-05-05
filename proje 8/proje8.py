import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QLabel, QTableWidget, QTableWidgetItem, QHBoxLayout, QDialog, QFormLayout, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

USERNAME = "admin"
PASSWORD = "admin"


class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Giriş Yap")
        layout = QFormLayout()
        
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.setGeometry(10, 40, 400, 165)
        self.setWindowIcon(QIcon('images.jpeg'))
        
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
            QTableWidget {
                selection-background-color: #4CAF50;
            }
            QLineEdit {
                border: 2px solid #4CAF50;
                padding: 5px;
            }
            QLabel {
                font-size: 16px;
            }
        """)

        
        layout.addRow("Kullanıcı Adı:", self.username_input)
        layout.addRow("Şifre:", self.password_input)
        
        login_button = QPushButton("Giriş Yap")
        login_button.clicked.connect(self.kontrol_et)
        
        layout.addWidget(login_button)
        self.setLayout(layout)
    
    def kontrol_et(self):
        if (self.username_input.text() == USERNAME and 
            self.password_input.text() == PASSWORD):
            self.accept()
        else:
            QMessageBox.warning(self, 'Hata', 'Yanlış kullanıcı adı veya şifre!')

class Urun:
    def __init__(self, urun_adi, stok_miktari, fiyat):
        self.urun_adi = urun_adi
        self.stok_miktari = stok_miktari
        self.fiyat = fiyat

    def to_dict(self):
        return {
            "urun_adi": self.urun_adi,
            "stok_miktari": self.stok_miktari,
            "fiyat": self.fiyat
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['urun_adi'], data['stok_miktari'], data['fiyat'])

    def urun_ekle(self, miktar):
        self.stok_miktari += miktar

    def siparis_olustur(self, miktar):
        if miktar <= self.stok_miktari:
            self.stok_miktari -= miktar
        else:
            raise ValueError("Yeterli stok bulunmamaktadır.")
        
    def stok_guncelle(self, yeni_miktar):
        self.stok_miktari = yeni_miktar

class Stok:
    def __init__(self):
        self.urunler = {}

    def urun_ekle(self, urun):
        self.urunler[urun.urun_adi] = urun

    def urun_bul(self, urun_adi):
        return self.urunler.get(urun_adi, None)

    def save_to_file(self, file_path):
        with open(file_path, 'w') as file:
            json.dump([urun.to_dict() for urun in self.urunler.values()], file, indent=4)

    def load_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                urunler = json.load(file)
                for urun_data in urunler:
                    urun = Urun.from_dict(urun_data)
                    self.urun_ekle(urun)
        except FileNotFoundError:
            pass

class StokDuzenleDialog(QDialog):
    def __init__(self, stok):
        super().__init__()
        self.stok = stok
        self.setWindowTitle("Stok Düzenleme")
        self.setGeometry(150, 150, 675, 300)
        self.setWindowIcon(QIcon('indir.jpeg'))
        
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
            QTableWidget {
                selection-background-color: #4CAF50;
            }
            QLineEdit {
                border: 2px solid #4CAF50;
                padding: 5px;
            }
            QLabel {
                font-size: 16px;
            }
        """)

        layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(5) 
        self.table.setHorizontalHeaderLabels(["Ürün Adı", "Stok Miktarı", "Mevcut Fiyat", "Yeni Stok Miktarı", "Yeni Fiyat"])
        self.fill_table()
        layout.addWidget(self.table)

        update_button = QPushButton("Stokları ve Fiyatları Güncelle")
        update_button.clicked.connect(self.update_stocks_and_prices)
        layout.addWidget(update_button)

        self.setLayout(layout)

    def fill_table(self):
        self.table.setRowCount(0)
        for urun_adi, urun in self.stok.urunler.items():
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(urun.urun_adi))
            self.table.setItem(row_position, 1, QTableWidgetItem(str(urun.stok_miktari)))
            self.table.setItem(row_position, 2, QTableWidgetItem(f"{urun.fiyat:.2f}"))
            new_stok_input = QLineEdit()
            new_fiyat_input = QLineEdit()
            self.table.setCellWidget(row_position, 3, new_stok_input)
            self.table.setCellWidget(row_position, 4, new_fiyat_input)

    def update_stocks_and_prices(self):
        for row in range(self.table.rowCount()):
            new_stok = self.table.cellWidget(row, 3).text()
            new_fiyat = self.table.cellWidget(row, 4).text()
            urun_adi = self.table.item(row, 0).text()
            urun = self.stok.urun_bul(urun_adi)
            if new_stok.isdigit():
                urun.stok_guncelle(int(new_stok))
            if new_fiyat.replace('.', '', 1).isdigit():
                urun.fiyat = float(new_fiyat)
        self.fill_table()

class StokTakipUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stok Takip Sistemi - Plus")
        self.setWindowIcon(QIcon('indir.jpeg'))

        self.setWindowTitle("Stok Takip Sistemi")
        self.setGeometry(100, 100, 600, 600)

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
            QTableWidget {
                selection-background-color: #4CAF50;
            }
            QLineEdit {
                border: 2px solid #4CAF50;
                padding: 5px;
            }
            QLabel {
                font-size: 16px;
            }
        """)

        self.layout = QVBoxLayout()
        self.setup_ui()
        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)
        self.stok = Stok()
        self.stok.load_from_file('stok_data.json')
        self.stok_goruntule()

    def setup_ui(self):
        self.urun_adi_input = QLineEdit()
        self.urun_adi_input.setPlaceholderText("Ürün Adı Giriniz")
        self.layout.addWidget(self.urun_adi_input)

        self.stok_miktari_input = QLineEdit()
        self.stok_miktari_input.setPlaceholderText("Stok Miktarı Giriniz")
        self.layout.addWidget(self.stok_miktari_input)

        self.fiyat_input = QLineEdit()
        self.fiyat_input.setPlaceholderText("Ürün Fiyatı Giriniz")
        self.layout.addWidget(self.fiyat_input)

        ekle_button = QPushButton("Ürün Ekle")
        ekle_button.clicked.connect(self.urun_ekle)
        self.layout.addWidget(ekle_button)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Ürün Adı", "Stok Miktarı", "Fiyat"])
        self.layout.addWidget(self.table)

        duzenle_button = QPushButton("Stok Düzenle")
        duzenle_button.clicked.connect(self.stok_duzenle)
        self.layout.addWidget(duzenle_button)

        kaydet_button = QPushButton("Stokları Kaydet")
        kaydet_button.clicked.connect(self.stoklari_kaydet)
        self.layout.addWidget(kaydet_button)

    def urun_ekle(self):
        urun_adi = self.urun_adi_input.text()
        stok_miktari_text = self.stok_miktari_input.text()
        fiyat_text = self.fiyat_input.text()
    
        if not stok_miktari_text.isdigit() or not fiyat_text.replace('.', '', 1).isdigit():
            QMessageBox.warning(self, "Geçersiz Giriş", "Lütfen stok miktarı ve fiyat için geçerli sayısal değerler giriniz.")
            return

        stok_miktari = int(stok_miktari_text)
        fiyat = float(fiyat_text)

        urun = Urun(urun_adi, stok_miktari, fiyat)
        self.stok.urun_ekle(urun)
        self.stok_goruntule()


    def stok_goruntule(self):
        self.table.setRowCount(0)
        for urun_adi, urun in self.stok.urunler.items():
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            item_name = QTableWidgetItem(urun.urun_adi)
            item_stock = QTableWidgetItem(str(urun.stok_miktari))
            item_price = QTableWidgetItem(f"{urun.fiyat:.2f}")

            item_name.setFlags(item_name.flags() & ~Qt.ItemIsEditable)
            item_stock.setFlags(item_stock.flags() & ~Qt.ItemIsEditable)
            item_price.setFlags(item_price.flags() & ~Qt.ItemIsEditable)

            self.table.setItem(row_position, 0, item_name)
            self.table.setItem(row_position, 1, item_stock)
            self.table.setItem(row_position, 2, item_price)

    def stok_duzenle(self):
        dialog = StokDuzenleDialog(self.stok)
        dialog.exec_()
        self.stok_goruntule()

    def stoklari_kaydet(self):
        self.stok.save_to_file('stok_data.json')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginDialog()
    
    if login.exec_() == QDialog.Accepted:
        window = StokTakipUI()
        window.show()
        sys.exit(app.exec_())