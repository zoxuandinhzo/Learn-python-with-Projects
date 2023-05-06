from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QPushButton,
    QHBoxLayout,
)
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QIcon
from PyQt5.QtCore import Qt
from googletrans import Translator
import sys


class TranslatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.setWindowTitle("Translator")
        self.setWindowIcon(QIcon(".\Learn python with Projects\\assets\\logo.ico"))
        self.setGeometry(0, 0, 500, 700)
        self.create_widgets()
        self.show()

    def create_widgets(self):
        layout = QVBoxLayout()
        pixmap = QPixmap(".\Learn python with Projects\\assets\\background.png")
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(pixmap))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        name_label = QLabel("Translator", self)
        name_label.setStyleSheet(
            "color: white; font-family: Transformers Movie; font-size: 30pt; font-weight: bold; background-color: rgba(0, 0, 0, 0);"
        )
        name_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(name_label)

        self.box = QTextEdit(self)
        self.box.setStyleSheet("font-family: ROBOTO; font-size: 15pt")
        layout.addWidget(self.box)

        self.box1 = QTextEdit(self)
        self.box1.setStyleSheet("font-family: ROBOTO; font-size: 15pt")
        layout.addWidget(self.box1)

        button_layout = QHBoxLayout()
        clear_button = QPushButton("Clear", self)
        clear_button.setStyleSheet("font-family: ROBOTO; font-size: 15pt")
        clear_button.clicked.connect(self.clear)
        button_layout.addWidget(clear_button)

        trans_button = QPushButton("Translate", self)
        trans_button.setStyleSheet("font-family: ROBOTO; font-size: 15pt")
        trans_button.clicked.connect(self.translate)
        button_layout.addWidget(trans_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def clear(self):
        self.box.clear()
        self.box1.clear()

    def translate(self):
        input_text = self.box.toPlainText()
        translator = Translator()
        translated_text = translator.translate(input_text, src="vi", dest="en").text
        self.box1.clear()
        self.box1.insertPlainText(translated_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    translator_app = TranslatorApp()
    sys.exit(app.exec_())
