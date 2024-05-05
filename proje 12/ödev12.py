import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QLineEdit, QTextEdit, QComboBox, QDialog, QMessageBox
from PyQt5.QtCore import QDateTime

class HealthTrackerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kişisel Sağlık Takip Uygulaması")
        self.setGeometry(100, 100, 400, 400)
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

        self.init_ui()
        self.health_data = []
        self.load_data()

    def init_ui(self):
        main_layout = QVBoxLayout()

        
        user_info_layout = QHBoxLayout()
        user_info_layout.addWidget(QLabel("Ad: "))
        self.name_input = QLineEdit()
        user_info_layout.addWidget(self.name_input)
        user_info_layout.addWidget(QLabel("Yaş: "))
        self.age_input = QLineEdit()
        user_info_layout.addWidget(self.age_input)
        user_info_layout.addWidget(QLabel("Cinsiyet: "))
        self.gender_combo = QComboBox()
        self.gender_combo.addItems(["Erkek", "Kadın"])
        user_info_layout.addWidget(self.gender_combo)

        main_layout.addLayout(user_info_layout)

        
        self.health_record_layout = QHBoxLayout()
        self.health_record_layout.addWidget(QLabel("Boy (cm): "))
        self.height_input = QLineEdit()
        self.health_record_layout.addWidget(self.height_input)
        self.health_record_layout.addWidget(QLabel("Kilo (kg): "))
        self.weight_input = QLineEdit()
        self.health_record_layout.addWidget(self.weight_input)
        main_layout.addLayout(self.health_record_layout)

        
        self.exercise_input = QTextEdit()
        self.exercise_input.setPlaceholderText("Egzersizleri girin (örn: Egzersiz Adı: Koşu, Süre: 30 dakika, Tekrar Sayısı: 3)")
        main_layout.addWidget(self.exercise_input)

     
        button_layout = QHBoxLayout()
        save_button = QPushButton("Kaydet")
        save_button.clicked.connect(self.save_data)
        button_layout.addWidget(save_button)

        view_button = QPushButton("Verileri Görüntüle")
        view_button.clicked.connect(self.view_data)
        button_layout.addWidget(view_button)

        main_layout.addLayout(button_layout)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def load_data(self):
        if os.path.exists("health_data.txt"):
            with open("health_data.txt", "r") as file:
                self.health_data = [line.strip() for line in file.readlines()]

    def save_data(self):
        name = self.name_input.text()
        age = self.age_input.text()
        gender = self.gender_combo.currentText()
        height = self.height_input.text()
        weight = self.weight_input.text()
        exercise_data = self.exercise_input.toPlainText()

        if name and age and height and weight:
            
            now = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")

            health_data = f"Boy: {height} cm, Kilo: {weight} kg\nTarih: {now}"

            
            health_report = f"Ad: {name}\nYaş: {age}\nCinsiyet: {gender}\n{health_data}\nEgzersizler:\n{exercise_data}"

            
            self.health_data.append(health_report)
            self.save_to_file()
            QMessageBox.information(self, "Bilgi", "Veriler kaydedildi.")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun.")

    def save_to_file(self):
        with open("health_data.txt", "w") as file:
            for data in self.health_data:
                file.write(data + "\n")

    def view_data(self):
        if self.health_data:
            data_page = DataPage(self.health_data)
            data_page.exec_()
        else:
            QMessageBox.information(self, "Bilgi", "Kaydedilmiş veri bulunmamaktadır.")

class DataPage(QDialog):
    def __init__(self, data):
        super().__init__()
        self.setWindowTitle("Veri Görüntüleme")
        self.data = data

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
        text_edit.setPlainText("\n\n".join(self.data))
        layout.addWidget(text_edit)

        button_layout = QHBoxLayout()
        close_button = QPushButton("Kapat")
        close_button.clicked.connect(self.close)
        button_layout.addWidget(close_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)
        self.setFixedSize(500, 400)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HealthTrackerApp()
    window.show()
    sys.exit(app.exec_())


