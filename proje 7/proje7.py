import sys
import pickle
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QListWidget, QComboBox, QMessageBox
from PyQt5.QtGui import QIcon

class Sporcu:
    def __init__(self, adi, spor_dali):
        self.adi = adi
        self.spor_dali = spor_dali
        self.antrenman_programi = []

    def program_olustur(self, antrenman):
        self.antrenman_programi.append(antrenman)

    def rapor_al(self):
        return [(antrenman.adi, antrenman.detaylar, antrenman.periyot) for antrenman in self.antrenman_programi]

class Antrenman:
    def __init__(self, adi, detaylar, periyot):
        self.adi = adi
        self.detaylar = detaylar
        self.periyot = periyot

class AntrenmanListesiDialog(QDialog):
    def __init__(self, sporcular, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Antrenman Listesi')
        self.setGeometry(100, 100, 400, 600)
        self.sporcular = sporcular
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        self.antrenman_list_widget = QListWidget(self)
        for sporcu in self.sporcular:
            for antrenman in sporcu.antrenman_programi:
                self.antrenman_list_widget.addItem(f"{sporcu.adi} - {antrenman.adi} - {antrenman.detaylar} - {antrenman.periyot}")
        layout.addWidget(self.antrenman_list_widget)
        self.setLayout(layout)

class SporApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sporcular = []
        self.setWindowTitle('Spor Takip Uygulaması')
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon('olimpiyat.png'))
        self.data_file = 'sporcular_data.pkl'

        self.initUI()
        self.load_data()

    def initUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        central_widget.setStyleSheet("""
            QWidget {
                background-color: #f5f5f5;
                color: #333333;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px;
                font-size: 16px;
                border-radius: 5px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QLineEdit, QComboBox {
                border: 2px solid #4CAF50;
                padding: 5px;
                margin: 5px;
                font-size: 14px;
            }
            QListWidget {
                background-color: #ffffff;
                border: 1px solid #cccccc;
            }
        """)

        self.sporcu_adi_input = QLineEdit(self)
        self.sporcu_adi_input.setPlaceholderText('Sporcu Adını Girin')
        self.spor_dali_combobox = QComboBox(self)
        self.spor_dali_combobox.addItems(["Futbol", "Basketbol", "Yüzme", "Tenis", "Atletizm"])
        self.add_sporcu_button = QPushButton('Sporcu Ekle', self)
        self.add_sporcu_button.clicked.connect(self.add_sporcu)

        self.sporcu_secim_combobox = QComboBox(self)
        self.periyot_combobox = QComboBox(self)
        self.periyot_combobox.addItems(["Günlük", "Haftalık", "Aylık"])
        self.antrenman_adi_input = QLineEdit(self)
        self.antrenman_adi_input.setPlaceholderText('Antrenman Adını Girin')
        self.antrenman_detaylari_input = QLineEdit(self)
        self.antrenman_detaylari_input.setPlaceholderText('Antrenman Detaylarını Girin')
        self.add_antrenman_button = QPushButton('Antrenman Ekle', self)
        self.add_antrenman_button.clicked.connect(self.add_antrenman)

        self.show_antrenman_button = QPushButton('Antrenmanları Göster', self)
        self.show_antrenman_button.clicked.connect(self.show_antrenmanlar)

        layout.addWidget(self.sporcu_adi_input)
        layout.addWidget(self.spor_dali_combobox)
        layout.addWidget(self.add_sporcu_button)
        layout.addWidget(self.sporcu_secim_combobox)
        layout.addWidget(self.periyot_combobox)
        layout.addWidget(self.antrenman_adi_input)
        layout.addWidget(self.antrenman_detaylari_input)
        layout.addWidget(self.add_antrenman_button)
        layout.addWidget(self.show_antrenman_button)
        central_widget.setLayout(layout)

    def update_sporcu_combobox(self):
        self.sporcu_secim_combobox.clear()
        self.sporcu_secim_combobox.addItems([sporcu.adi for sporcu in self.sporcular])

    def add_sporcu(self):
        sporcu_adi = self.sporcu_adi_input.text().strip()
        if not sporcu_adi:
            QMessageBox.warning(self, "Gerekli Alan", "Lütfen sporcu adını girin.")
            return

        spor_dali = self.spor_dali_combobox.currentText()
        yeni_sporcu = Sporcu(sporcu_adi, spor_dali)
        self.sporcular.append(yeni_sporcu)
        self.update_sporcu_combobox()
        self.sporcu_adi_input.clear()
        self.save_data()

    def add_antrenman(self):
        if not self.sporcular:
            QMessageBox.warning(self, "Sporcu Yok", "Önce sporcu ekleyin.")
            return

        secili_sporcu_adi = self.sporcu_secim_combobox.currentText()
        secili_sporcu = next((sporcu for sporcu in self.sporcular if sporcu.adi == secili_sporcu_adi), None)
        if secili_sporcu is None:
            QMessageBox.warning(self, "Sporcu Bulunamadı", "Seçili sporcu bulunamadı.")
            return

        antrenman_adi = self.antrenman_adi_input.text().strip()
        antrenman_detaylari = self.antrenman_detaylari_input.text().strip()
        if not antrenman_adi or not antrenman_detaylari:
            QMessageBox.warning(self, "Gerekli Alanlar", "Lütfen antrenman adı ve detaylarını girin.")
            return

        periyot = self.periyot_combobox.currentText()
        yeni_antrenman = Antrenman(antrenman_adi, antrenman_detaylari, periyot)
        secili_sporcu.program_olustur(yeni_antrenman)
        self.save_data()

    def show_antrenmanlar(self):
        dialog = AntrenmanListesiDialog(self.sporcular, parent=self)
        dialog.exec_()

    def save_data(self):
        with open(self.data_file, 'wb') as f:
            pickle.dump(self.sporcular, f)

    def load_data(self):
        try:
            with open(self.data_file, 'rb') as f:
                self.sporcular = pickle.load(f)
                self.update_sporcu_combobox()
        except FileNotFoundError:
            print("Henüz veri dosyası oluşturulmadı.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = SporApp()
    mainWin.show()
    sys.exit(app.exec_())