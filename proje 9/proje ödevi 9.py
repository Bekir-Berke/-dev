import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QComboBox, QHBoxLayout, QListWidget, QListWidgetItem, QStackedWidget, QMessageBox
from PyQt5.QtGui import QIcon

class SeyahatPlanlamaUygulamasiUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setWindowTitle("Seyahat Planlama Uygulaması")
        self.setGeometry(100, 100, 400, 300)
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

        self.planlar = []  # List to store selected plans

        layout = QVBoxLayout()

        self.label = QLabel("Seyahat Planı Oluştur")
        layout.addWidget(self.label)

        self.setWindowIcon(QIcon('images.jpg'))

        self.rota_combo = QComboBox()
        self.rota_combo.addItems(["İstanbul - İzmir - Antalya", "İstanbul - İzmir - Gaziantep", "İzmir - Antalya - Bodrum", "Ankara - Trabzon - Eskişehir", "İzmit - Adana - Antalya"])
        self.rota_combo.currentIndexChanged.connect(self.guncel_otel_listesi)
        layout.addWidget(self.rota_combo)

        self.kutu1_label = QLabel("")
        layout.addWidget(self.kutu1_label)
        self.kutu1 = QComboBox()
        layout.addWidget(self.kutu1)

        self.kutu2_label = QLabel("")
        layout.addWidget(self.kutu2_label)
        self.kutu2 = QComboBox()
        layout.addWidget(self.kutu2)

        self.kutu3_label = QLabel("")
        layout.addWidget(self.kutu3_label)
        self.kutu3 = QComboBox()
        layout.addWidget(self.kutu3)

        self.plan_ekle_button = QPushButton("Plan Ekle")
        self.plan_ekle_button.setStyleSheet("font-size: 16px; color: #fff; background-color: #6bbf5b; border: none; padding: 10px 20px; border-radius: 5px;")
        self.plan_ekle_button.clicked.connect(self.plan_ekle)
        layout.addWidget(self.plan_ekle_button)

        self.plani_goster_button = QPushButton("Planları Gör")
        self.plani_goster_button.setStyleSheet("font-size: 16px; color: #fff; background-color: #3498db; border: none; padding: 10px 20px; border-radius: 5px;")
        self.plani_goster_button.clicked.connect(self.plani_goster)
        layout.addWidget(self.plani_goster_button)

        self.setLayout(layout)

        self.otel_listeleri = {
            "İstanbul": {"Park Inn by Radisson Istanbul Ataturk Airport": 1889, "Peralas Otel Bağcılar": 980},
            "İzmir": {"Wyndham Grand Izmir Özdilek": 4492, "İzmir Plaza Otel": 1749},
            "Antalya": {"Prime Hotel": 3099, "Can Adalya Palace Hotel": 1816},
            "Gaziantep": {"Hampton by Hilton Gaziantep": 4885, "Yeni Erciyes Gold Hotel & SPA": 850},
            "Bodrum": {"Tropicana Beach Hotel": 2099, "Museum Resort Spa": 1739},
            "Ankara": {"Ankara HiltonSA": 2000, "Swissotel Ankara": 1500},
            "Trabzon": {"Novotel Trabzon": 2500, "Zorlu Grand Hotel Trabzon": 1800},
            "Eskişehir": {"The Merlot Hotel": 1600, "Hotel Ibis Eskisehir": 1200},
            "İzmit": {"Luxor Garden Hotel": 1500, "Green Park Resort Kartepe": 1000},
            "Adana": {"Sheraton Grand Adana": 2200, "Divan Adana": 1600}
        }

    def guncel_otel_listesi(self):
        secilen_rota = self.rota_combo.currentText()
        sehirler = secilen_rota.split(" - ")

        self.kutu1_label.setText(f"{sehirler[0]} için otel seçimi:")
        self.kutu1.clear()
        for otel, fiyat in self.otel_listeleri[sehirler[0]].items():
            self.kutu1.addItem(f"{otel} - {fiyat} TL")

        self.kutu2_label.setText(f"{sehirler[1]} için otel seçimi:")
        self.kutu2.clear()
        for otel, fiyat in self.otel_listeleri[sehirler[1]].items():
            self.kutu2.addItem(f"{otel} - {fiyat} TL")

        self.kutu3_label.setText(f"{sehirler[2]} için otel seçimi:")
        self.kutu3.clear()
        for otel, fiyat in self.otel_listeleri[sehirler[2]].items():
            self.kutu3.addItem(f"{otel} - {fiyat} TL")

    def plan_ekle(self):
        # Plan eklenmeden önce onay iletişim kutusunu göster
        onay = QMessageBox.question(self, 'Onay', 'Planı eklemek istediğinizden emin misiniz?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if onay == QMessageBox.Yes:
            secilen_rota = self.rota_combo.currentText()     
            secilen_sehirler = secilen_rota.split(" - ") 
            secilen_otel1 = self.kutu1.currentText().split(" - ")[0] 
            secilen_otel2 = self.kutu2.currentText().split(" - ")[0] 
            secilen_otel3 = self.kutu3.currentText().split(" - ")[0]

            self.planlar.append((secilen_sehirler[0], secilen_otel1, secilen_sehirler[1], secilen_otel2, secilen_sehirler[2], secilen_otel3))

    def plani_goster(self):
        self.plan_listesi = PlanListesi(self.planlar)
        self.plan_listesi.show()


class PlanListesi(QWidget):
    def __init__(self, planlar):
        super().__init__()
        self.setWindowTitle("Planlar Listesi")
        self.setGeometry(300, 300, 400, 300)

        self.planlar = planlar  # 'planlar' özelliğini tanımla

        layout = QVBoxLayout()

        self.label = QLabel("Eklenen Planlar")
        self.label.setStyleSheet("font-size: 24px; font-weight: bold; color: #444;")
        layout.addWidget(self.label)

        self.planlar_list_widget = QListWidget()
        layout.addWidget(self.planlar_list_widget)

        self.geri_don_button = QPushButton("Geri Dön")
        self.geri_don_button.setStyleSheet("font-size: 16px; color: #fff; background-color: #3498db; border: none; padding: 10px 20px; border-radius: 5px;")
        self.geri_don_button.clicked.connect(self.geri_don)
        layout.addWidget(self.geri_don_button)

        self.plan_sil_button = QPushButton("Planı Sil")
        self.plan_sil_button.setStyleSheet("font-size: 16px; color: #fff; background-color: #e74c3c; border: none; padding: 10px 20px; border-radius: 5px;")
        self.plan_sil_button.clicked.connect(self.plan_sil)
        layout.addWidget(self.plan_sil_button)

        self.setLayout(layout)

        for plan in planlar:
            self.planlar_list_widget.addItem(f"Seyahat Planı: {plan}")

    def plan_sil(self):
        secili_ogeler = self.planlar_list_widget.selectedItems()
        if not secili_ogeler:
            return

        indeks = self.planlar_list_widget.row(secili_ogeler[0])

        self.planlar_list_widget.takeItem(indeks)
        del self.planlar[indeks]

    def geri_don(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SeyahatPlanlamaUygulamasiUI()
    window.show()
    sys.exit(app.exec_())
