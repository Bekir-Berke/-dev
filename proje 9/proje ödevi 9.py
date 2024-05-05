import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QComboBox, QHBoxLayout
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
        secilen_rota = self.rota_combo.currentText()
        secilen_sehirler = secilen_rota.split(" - ")
        secilen_otel1 = self.kutu1.currentText().split(" - ")[0]
        secilen_otel2 = self.kutu2.currentText().split(" - ")[0]
        secilen_otel3 = self.kutu3.currentText().split(" - ")[0]

        self.plan_arayuzu = PlanArayuzu(secilen_sehirler[0], secilen_otel1, secilen_sehirler[1], secilen_otel2, secilen_sehirler[2], secilen_otel3)
        self.plan_arayuzu.show()

class PlanArayuzu(QWidget):
    def __init__(self, sehir1, otel1, sehir2, otel2, sehir3, otel3):
        super().__init__()
        self.setWindowIcon(QIcon('images.jpg'))
        self.setWindowTitle("Plan Detayları")
        self.setGeometry(200, 200, 400, 300)
        self.setStyleSheet("background-color: #f5f5f5; border-radius: 10px;")

        layout = QVBoxLayout()

        self.label = QLabel("Seçtiğiniz Plan:")
        self.label.setStyleSheet("font-size: 24px; font-weight: bold; color: #444;")
        layout.addWidget(self.label)

        self.plan_detay_label = QLabel(f"Şehirler: {sehir1} - {sehir2} - {sehir3}\nOtel Seçimleri: {otel1}, {otel2}, {otel3}")
        self.plan_detay_label.setStyleSheet("font-size: 16px; color: #444;")
        layout.addWidget(self.plan_detay_label)

        self.buttons_layout = QHBoxLayout()

        self.kabul_button = QPushButton("Kabul Ediyorum")
        self.kabul_button.setStyleSheet("font-size: 16px; color: #fff; background-color: #6bbf5b; border: none; padding: 10px 20px; border-radius: 5px;")
        self.kabul_button.clicked.connect(self.kabul_edildi)
        self.buttons_layout.addWidget(self.kabul_button)

        self.geri_don_button = QPushButton("Rota Seçmeye Geri Dön")
        self.geri_don_button.setStyleSheet("font-size: 16px; color: #fff; background-color: #f77676; border: none; padding: 10px 20px; border-radius: 5px;")
        self.geri_don_button.clicked.connect(self.geri_don)
        self.buttons_layout.addWidget(self.geri_don_button)

        layout.addLayout(self.buttons_layout)

        self.setLayout(layout)

    def kabul_edildi(self):
        self.plan_tamamlandi = PlanTamamlandi()
        self.plan_tamamlandi.show()
        self.close()

    def geri_don(self):
        self.close()

class PlanTamamlandi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('images.jpg'))
        self.setWindowTitle("Plan Tamamlandı")
        self.setGeometry(300, 300, 200, 100)
        self.setStyleSheet("background-color: #f5f5f5; border-radius: 10px;")

        layout = QVBoxLayout()

        self.label = QLabel("Planınız başarıyla tamamlandı!")
        self.label.setStyleSheet("font-size: 24px; font-weight: bold; color: #444;")
        layout.addWidget(self.label)

        self.tamam_button = QPushButton("Tamam")
        self.tamam_button.setStyleSheet("font-size: 16px; color: #fff; background-color: #6bbf5b; border: none; padding: 10px 20px; border-radius: 5px;")
        self.tamam_button.clicked.connect(self.tamam)
        layout.addWidget(self.tamam_button)

        self.setLayout(layout)

    def tamam(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SeyahatPlanlamaUygulamasiUI()
    window.show()
    sys.exit(app.exec_())
