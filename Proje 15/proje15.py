import sys
from PyQt5.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QWidget, QPushButton, QLabel,
    QTextEdit, QListWidget, QHBoxLayout, QLineEdit, QMessageBox,
)
from PyQt5.QtGui import QColor, QIcon 


class Book:
    def __init__(self, title, author, publisher, story):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.comments = []
        self.story = story

    def read_book(self):
        return self.story

    def add_comment(self, user, comment_text):
        comment = Comment(comment_text, user)
        self.comments.append(comment)


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.reading_list = []

    def add_to_reading_list(self, book):
        self.reading_list.append(book)


class Comment:
    def __init__(self, text, user):
        self.text = text
        self.user = user


class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Çevrimiçi Kitap Okuma ve Paylaşım Platformu")
        self.setGeometry(200, 200, 300, 200)
        self.setStyleSheet("background-color: #f0f0f0;")
        self.setWindowIcon(QIcon("images.png"))
        self.layout = QVBoxLayout(self)

        self.login_label = QLabel("Giriş Yap", self)
        self.login_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.layout.addWidget(self.login_label)

        self.user_label = QLabel("Kullanıcı Adı:", self)
        self.layout.addWidget(self.user_label)

        self.user_edit = QLineEdit(self)
        self.user_edit.setStyleSheet("background-color: #ffffff; border: 1px solid #cccccc;")
        self.layout.addWidget(self.user_edit)

        self.password_label = QLabel("Şifre:", self)
        self.layout.addWidget(self.password_label)

        self.password_edit = QLineEdit(self)
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.password_edit.setStyleSheet("background-color: #ffffff; border: 1px solid #cccccc;")
        self.layout.addWidget(self.password_edit)
        self.login_button = QPushButton("Giriş Yap", self)
        self.login_button.setStyleSheet("background-color: #4CAF50; color: white; border: none; padding: 8px 16px; border-radius: 4px;")
        self.layout.addWidget(self.login_button)
        self.login_button.clicked.connect(self.login)

    def login(self):
        username = self.user_edit.text()
        password = self.password_edit.text()
        if username and password:
            self.accept()
        else:
            QMessageBox.warning(self, "Uyarı", "Kullanıcı adı ve şifre girin.")


class BookPlatform(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Çevrimiçi Kitap Okuma ve Paylaşım Platformu")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #f0f0f0;")
        self.setWindowIcon(QIcon("icon.jpg"))

        self.books = {
            "Python Programlama": Book("Python Programlama", "İbrahim Aydın", "14 Yayınevi",
                                        "Python Programlama kitabı temel Python programlama konularını kapsamaktadır."),
            "Algoritma ve Veri Yapıları": Book("Algoritma ve Veri Yapıları", "Erdem Yücesan", "Kültür Yayınevi",
                                                "Algoritma ve Veri Yapıları kitabı temel algoritma ve veri yapıları konularını içermektedir."),
            "Yüzyıllık Yalnızlık": Book("Yüzyıllık Yalnızlık", "Gabriel Garcia Marquez", "YKY",
                                        "Büyüleyici bir aile hikayesi olan Yüzyıllık Yalnızlık, Latin Amerika edebiyatının başyapıtlarından biridir."),
            "1984": Book("1984", "George Orwell", "Can Yayınları",
                         "Distopik bir geleceği konu alan 1984, bireyin özgürlüğü ve devlet kontrolü arasındaki çatışmayı işler."),
            "Dönüşüm": Book("Dönüşüm", "Franz Kafka", "İthaki Yayınları",
                            "Kafka'nın en önemli eserlerinden biri olan Dönüşüm, Gregor Samsa'nın bir böceğe dönüşmesini anlatır."),
            "Sapiens": Book("Sapiens", "Yuval Noah Harari", "Kolektif Kitap",
                            "İnsan tarihini geniş bir perspektiften ele alan Sapiens, modern insanın evrimini inceler."),
            "Harry Potter ve Felsefe Taşı": Book("Harry Potter ve Felsefe Taşı", "J.K. Rowling", "Yapı Kredi Yayınları",
                                                 "Harry Potter serisinin ilk kitabı olan Felsefe Taşı, büyülü bir dünyaya girişi anlatır."),
            "Hayvan Çiftliği": Book("Hayvan Çiftliği", "George Orwell", "Can Yayınları",
                                    "Siyasi bir alegori olan Hayvan Çiftliği, hayvanların yönetiminde yaşanan değişimleri anlatır."),
            "Kuyucaklı Yusuf": Book("Kuyucaklı Yusuf", "Sabahattin Ali", "İş Bankası Kültür Yayınları",
                                     "Bir aşk ve ahlak öyküsü olan Kuyucaklı Yusuf, Sabahattin Ali'nin önemli eserlerinden biridir.")
        }
        self.current_book = None
        self.current_user = None

        self.layout = QVBoxLayout(self)

        self.book_list = QListWidget(self)
        self.book_list.setStyleSheet("background-color: #ffffff; border: 1px solid #cccccc;")
        self.book_list.addItems(self.books.keys())
        self.book_list.itemClicked.connect(self.load_book_info)
        self.layout.addWidget(self.book_list)

        self.book_info_label = QLabel("", self)
        self.layout.addWidget(self.book_info_label)

        self.comment_label = QLabel("Yorum Yap:", self)
        self.layout.addWidget(self.comment_label)

        self.comment_text = QLineEdit(self)
        self.comment_text.setStyleSheet("background-color: #ffffff; border: 1px solid #cccccc;")
        self.layout.addWidget(self.comment_text)

        self.comment_button = QPushButton("Yorum Yap", self)
        self.comment_button.setStyleSheet("background-color: #4CAF50; color: white; border: none; padding: 8px 16px; border-radius: 4px;")
        self.comment_button.clicked.connect(self.add_comment)
        self.layout.addWidget(self.comment_button)

        self.comment_display = QTextEdit(self)
        self.comment_display.setStyleSheet("background-color: #ffffff; border: 1px solid #cccccc;")
        self.comment_display.setReadOnly(True)
        self.layout.addWidget(self.comment_display)

        self.read_button = QPushButton("Kitap İçeriğini Göster", self)
        self.read_button.setStyleSheet("background-color: #2196F3; color: white; border: none; padding: 8px 16px; border-radius: 4px;")
        self.read_button.clicked.connect(self.read_book)
        self.layout.addWidget(self.read_button)

        self.share_button = QPushButton("Kitabı Paylaş", self)
        self.share_button.setStyleSheet("background-color: #FF9800; color: white; border: none; padding: 8px 16px; border-radius: 4px;")
        self.share_button.clicked.connect(self.share_book)
        self.layout.addWidget(self.share_button)

    def load_book_info(self, item):
        book_title = item.text()
        self.current_book = self.books[book_title]
        self.book_info_label.setText(f"Yazar: {self.current_book.author}\nYayınevi: {self.current_book.publisher}")
        self.update_comment_display()

    def add_comment(self):
        if self.current_book and self.current_user:
            comment_text = self.comment_text.text()
            self.current_book.add_comment(self.current_user, comment_text)
            self.comment_text.clear()
            self.update_comment_display()
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir kitap seçin ve kullanıcı girişi yapın.")

    def update_comment_display(self):
        if self.current_book:
            comments_info = "\n".join([f"{comment.user.username} tarafından yapılan yorum: {comment.text}" for comment in self.current_book.comments])
            self.comment_display.setPlainText(comments_info)

    def read_book(self):
        if self.current_book:
            QMessageBox.information(self, "Kitap İçeriği", self.current_book.read_book())
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir kitap seçin.")

    def share_book(self):
        if self.current_book and self.current_user:
            self.current_user.add_to_reading_list(self.current_book)
            QMessageBox.information(self, "Kitap Paylaşımı", f"{self.current_book.title} kitabı {self.current_user.username} tarafından paylaşıldı.")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir kitap seçin ve kullanıcı girişi yapın.")

    def show_login_dialog(self):
        login_dialog = LoginDialog()
        if login_dialog.exec_() == QDialog.Accepted:
            self.current_user = User(login_dialog.user_edit.text(), login_dialog.password_edit.text())
            QMessageBox.information(self, "Giriş Başarılı", f"{self.current_user.username} kullanıcısı olarak giriş yapıldı.")
            self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_dialog = LoginDialog()
    if login_dialog.exec_() == QDialog.Accepted:
        window = BookPlatform()
        window.show_login_dialog()
        sys.exit(app.exec_())
