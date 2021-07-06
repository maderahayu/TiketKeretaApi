from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QLabel, QPushButton
from beliTiket import beliTiket

class homeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setStyleSheet("""
                            QWidget {background-color: rgb(45, 79, 108);}
                            QPushButton {background-color: beige;}
                        """)

        self.setWindowTitle("LINGKAR INDONESIA - PENJUALAN TIKET KERETA API")
        self.setWindowIcon(QIcon('img/logoKereta.png'))
        self.setGeometry(0, 0, 650, 450)

        frame = self.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(center)
        self.move(frame.topLeft())

        self.label = QLabel(self)
        self.pixmap = QPixmap('img/logoKereta.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(), self.pixmap.height())

        self.btnCari = QPushButton('Cari Tiket', self)
        self.btnCari.setGeometry(QRect(540, 200, 80, 23))
        self.btnCari.clicked.connect(self.btnCariClicked)

    def btnCariClicked(self):
        self.beliTiket = beliTiket()
        self.hide()
        self.beliTiket.show()
