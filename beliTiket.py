import sys
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QIcon
from PyQt5.QtPrintSupport import QPrintPreviewDialog
from PyQt5.QtWidgets import QLabel, QWidget, QDesktopWidget, QComboBox, QLineEdit, QPushButton, QInputDialog, QTextEdit

class beliTiket(QWidget):
    def __init__(self):
        super().__init__()
        self.setUi()
        self.inputan()

    def setUi(self):
        self.setWindowTitle("LINGKAR INDONESIA - PENJUALAN TIKET KERETA API")
        self.setWindowIcon(QIcon('img/logoKereta.png'))
        self.setGeometry(0, 0, 400, 400)

        self.setStyleSheet("""
        QWidget {background-color: rgb(45, 79, 108);}
        QLabel{
                color: #ffffff;
                font-size: 10pt;
                border-radius: 2px;}
        QLineEdit, QTextEdit{
                background-color: rgb(255, 255, 255);
                color: rgb(0, 0, 0);
                border-radius: 2px;
                font-size: 10pt;
                border: none;}
        QPushButton{
                background-color: rgb(255, 255, 255);
                font-size: 10pt;
                border: none;}
        QComboBox{
                background-color: rgb(255, 255, 255);
                background: rgb(255, 255, 255);
                alternate-background-color: rgb(255, 255, 255);
                border-radius: 2px;}
        QCombobox::down-arrow{
            image:url('img/dropDown.png')
            border-radius:2px;}
        """)
        frame = self.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(center)
        self.move(frame.topLeft())

    def inputan(self):
        global jmlPenumpangDrop
        jmlPenumpangDrop = ('1', '2', '3', '4')
        self.selection, self.ok = QInputDialog.getItem(self, "Pilih Jumlah Penumpang", "Jumlah Penumpang", jmlPenumpangDrop, 0, False)

        self.jmltPenumpangtxt = QLabel('Jumlah Penumpang: ', self)
        self.jmltPenumpangtxt.setGeometry(10, 35, 120, 25)

        if self.ok == False:
            sys.exit()
        else:
            if self.selection == jmlPenumpangDrop[0]:
                self.jmlPenumpang01PNP = QLabel(jmlPenumpangDrop[0] + ' orang', self)
                self.jmlPenumpang01PNP.setGeometry(130, 35, 50, 25)
                self.namatxt01PNP = QLabel('Nama Penumpang:', self)
                self.namatxt01PNP.setGeometry(QRect(10, 60, 120, 25))
                self.namatxtLineEdit01PNP = QLineEdit(self)
                self.namatxtLineEdit01PNP.setGeometry(10, 85, 300, 25)
                self.asaltxt01PNP = QLabel('Asal:', self)
                self.asaltxt01PNP.setGeometry(QRect(10, 110, 120, 25))
                self.asalcb01PNP = QComboBox(self)
                self.asalcb01PNP.setGeometry(QRect(10, 135, 100, 25))
                self.asalcb01PNP.addItems(['Surabaya', 'Solo', 'Banyuwangi'])
                self.tujuantxt01PNP = QLabel('Tujuan:', self)
                self.tujuantxt01PNP.setGeometry(QRect(200, 110, 120, 25))
                self.tujuancb01PNP = QComboBox(self)
                self.tujuancb01PNP.setGeometry(QRect(200, 135, 100, 25))
                self.tujuancb01PNP.addItems(['Surabaya', 'Solo', 'Banyuwangi'])
                self.btnTampilkan01PNP = QPushButton("Tampilkan", self)
                self.btnTampilkan01PNP.setGeometry(300, 300, 80, 25)
                self.btnTampilkan01PNP.clicked.connect(self.btnTampilkanClicked)
                self.tampilanTiket01PNP = QTextEdit(self)
                self.tampilanTiket01PNP.setGeometry(10, 195, 270, 180)
                self.tampilanTiket01PNP.setReadOnly(True)
                self.btnCetak01PNP = QPushButton('Cetak Tiket', self)
                self.btnCetak01PNP.setGeometry(300, 350, 80, 25)
                self.btnCetak01PNP.clicked.connect(self.btnCetakClicked)
            elif self.selection == jmlPenumpangDrop[1]: #Jika jumlah penumpang ada 2

                self.jmlPenumpang02PNP = QLabel(jmlPenumpangDrop[1] + ' orang', self)
                self.jmlPenumpang02PNP.setGeometry(130, 35, 50, 25)

                self.namatxt02PNPA = QLabel('Nama Penumpang 1:', self)
                self.namatxt02PNPA.setGeometry(QRect(10, 60, 120, 25))
                self.namatxt02PNPB = QLabel('Nama Penumpang 2:', self)
                self.namatxt02PNPB.setGeometry(QRect(200, 60, 120, 25))

                self.namatxtLineEdit02PNPA = QLineEdit(self)
                self.namatxtLineEdit02PNPA.setGeometry(10, 85, 150, 25)
                self.namatxtLineEdit02PNPB = QLineEdit(self)
                self.namatxtLineEdit02PNPB.setGeometry(200, 85, 150, 25)

                self.asaltxt02PNP = QLabel('Asal:', self)
                self.asaltxt02PNP.setGeometry(QRect(10, 110, 120, 25))
                self.asalcb02PNP = QComboBox(self)
                self.asalcb02PNP.setGeometry(QRect(10, 135, 100, 25))
                self.asalcb02PNP.addItems(['Surabaya', 'Solo', 'Banyuwangi'])

                self.tujuantxt02PNP = QLabel('Tujuan:', self)
                self.tujuantxt02PNP.setGeometry(QRect(200, 110, 120, 25))
                self.tujuancb02PNP = QComboBox(self)
                self.tujuancb02PNP.setGeometry(QRect(200, 135, 100, 25))
                self.tujuancb02PNP.addItems(['Surabaya', 'Solo', 'Banyuwangi'])

                self.btnTampilkan02PNP = QPushButton("Tampilkan", self)
                self.btnTampilkan02PNP.setGeometry(300, 300, 80, 25)
                self.btnTampilkan02PNP.clicked.connect(self.btnTampilkanClicked)

                self.tampilanTiket02PNP = QTextEdit(self)
                self.tampilanTiket02PNP.setGeometry(10, 195, 270, 180)
                self.tampilanTiket02PNP.setReadOnly(True)

                self.btnCetak02PNP = QPushButton('Cetak Tiket', self)
                self.btnCetak02PNP.setGeometry(300, 350, 80, 25)
                self.btnCetak02PNP.clicked.connect(self.btnCetakClicked)
            elif self.selection == jmlPenumpangDrop[2]: #Jika jumlah penumpang ada 3

                self.jmlPenumpang03PNP = QLabel(jmlPenumpangDrop[2] + ' orang', self)
                self.jmlPenumpang03PNP.setGeometry(130, 35, 50, 25)

                self.namatxt03PNPA = QLabel('Nama Penumpang 1:', self)
                self.namatxt03PNPA.setGeometry(QRect(10, 60, 120, 25))
                self.namatxt03PNPB = QLabel('Nama Penumpang 2:', self)
                self.namatxt03PNPB.setGeometry(QRect(200, 60, 120, 25))
                self.namatxt03PNPC = QLabel('Nama Penumpang 3:', self)
                self.namatxt03PNPC.setGeometry(QRect(10, 110, 120, 25))

                self.namatxtLineEdit03PNPA = QLineEdit(self)
                self.namatxtLineEdit03PNPA.setGeometry(10, 85, 150, 25)
                self.namatxtLineEdit03PNPB = QLineEdit(self)
                self.namatxtLineEdit03PNPB.setGeometry(200, 85, 150, 25)
                self.namatxtLineEdit03PNPC = QLineEdit(self)
                self.namatxtLineEdit03PNPC.setGeometry(10, 135, 150, 25)

                self.asaltxt03PNP = QLabel('Asal:', self)
                self.asaltxt03PNP.setGeometry(QRect(10, 165, 120, 25))
                self.asalcb03PNP = QComboBox(self)
                self.asalcb03PNP.setGeometry(QRect(10, 190, 100, 25))
                self.asalcb03PNP.addItems(['Surabaya', 'Solo', 'Banyuwangi'])

                self.tujuantxt03PNP = QLabel('Tujuan:', self)
                self.tujuantxt03PNP.setGeometry(QRect(200, 165, 120, 25))
                self.tujuancb03PNP = QComboBox(self)
                self.tujuancb03PNP.setGeometry(QRect(200, 190, 100, 25))
                self.tujuancb03PNP.addItems(['Surabaya', 'Solo', 'Banyuwangi'])
                #
                self.btnTampilkan03PNP = QPushButton("Tampilkan", self)
                self.btnTampilkan03PNP.setGeometry(300, 300, 80, 25)
                self.btnTampilkan03PNP.clicked.connect(self.btnTampilkanClicked)

                self.tampilanTiket03PNP = QTextEdit(self)
                self.tampilanTiket03PNP.setGeometry(10, 235, 270, 140)
                self.tampilanTiket03PNP.setReadOnly(True)

                self.btnCetak03PNP = QPushButton('Cetak Tiket', self)
                self.btnCetak03PNP.setGeometry(300, 350, 80, 25)
                self.btnCetak03PNP.clicked.connect(self.btnCetakClicked)
            elif self.selection == jmlPenumpangDrop[3]: #Jika Jumlah Penumpang ada 4
                self.jmlPenumpang04PNP = QLabel(jmlPenumpangDrop[3] + ' orang', self)
                self.jmlPenumpang04PNP.setGeometry(130, 35, 50, 25)

                self.namatxt04PNPA = QLabel('Nama Penumpang 1:', self)
                self.namatxt04PNPA.setGeometry(QRect(10, 60, 120, 25))
                self.namatxt04PNPB = QLabel('Nama Penumpang 2:', self)
                self.namatxt04PNPB.setGeometry(QRect(200, 60, 120, 25))
                self.namatxt04PNPC = QLabel('Nama Penumpang 3:', self)
                self.namatxt04PNPC.setGeometry(QRect(10, 110, 120, 25))
                self.namatxt04PNPD = QLabel('Nama Penumpang 4:', self)
                self.namatxt04PNPD.setGeometry(QRect(200, 110, 120, 25))

                self.namatxtLineEdit04PNPA = QLineEdit(self)
                self.namatxtLineEdit04PNPA.setGeometry(10, 85, 150, 25)
                self.namatxtLineEdit04PNPB = QLineEdit(self)
                self.namatxtLineEdit04PNPB.setGeometry(200, 85, 150, 25)
                self.namatxtLineEdit04PNPC = QLineEdit(self)
                self.namatxtLineEdit04PNPC.setGeometry(10, 135, 150, 25)
                self.namatxtLineEdit04PNPD = QLineEdit(self)
                self.namatxtLineEdit04PNPD.setGeometry(200, 135, 150, 25)

                self.asaltxt04PNP = QLabel('Asal:', self)
                self.asaltxt04PNP.setGeometry(QRect(10, 165, 120, 25))
                self.asalcb04PNP = QComboBox(self)
                self.asalcb04PNP.setGeometry(QRect(10, 190, 100, 25))
                self.asalcb04PNP.addItems(['Surabaya', 'Solo', 'Banyuwangi'])

                self.tujuantxt04PNP = QLabel('Tujuan:', self)
                self.tujuantxt04PNP.setGeometry(QRect(200, 165, 120, 25))
                self.tujuancb04PNP = QComboBox(self)
                self.tujuancb04PNP.setGeometry(QRect(200, 190, 100, 25))
                self.tujuancb04PNP.addItems(['Surabaya', 'Solo', 'Banyuwangi'])

                self.btnTampilkan04PNP = QPushButton("Tampilkan", self)
                self.btnTampilkan04PNP.setGeometry(300, 300, 80, 25)
                self.btnTampilkan04PNP.clicked.connect(self.btnTampilkanClicked)

                self.tampilanTiket04PNP = QTextEdit(self)
                self.tampilanTiket04PNP.setGeometry(10, 235, 270, 140)
                self.tampilanTiket04PNP.setReadOnly(True)

                self.btnCetak = QPushButton('Cetak Tiket', self)
                self.btnCetak.setGeometry(300, 350, 80, 25)
                self.btnCetak.clicked.connect(self.btnCetakClicked)

    def btnTampilkanClicked(self):
        Harga = (100000, 150000, 350000)
        if self.selection == jmlPenumpangDrop[0]:
            self.asal, self.tujuan = self.asalcb01PNP.currentText(), self.tujuancb01PNP.currentText()
            self.nama01PNP = self.namatxtLineEdit01PNP.text()
            self.tampilanTiket01PNP.clear()
            self.tampilanTiket01PNP.append("Tiket untuk "+ jmlPenumpangDrop[0]+" Penumpang")
            self.tampilanTiket01PNP.append("\n<u>Penumpang 01</u>")
            self.tampilanTiket01PNP.append("Nama\t: "+ self.nama01PNP)
            if self.asal == 'Surabaya' and self.tujuan == 'Solo':
                self.tampilanTiket01PNP.append("Asal\t: "+ self.asal)
                self.tampilanTiket01PNP.append("Tujuan\t: "+ self.tujuan)
                self.tampilanTiket01PNP.append("Harga\t: Rp. "+ str(Harga[0]))
                self.tampilanTiket01PNP.append("Harga Total\t: Rp. " + str(Harga[0]*1))
            elif self.asal == 'Solo' and self.tujuan == 'Surabaya':
                self.tampilanTiket01PNP.append("Asal\t: "+ self.asal)
                self.tampilanTiket01PNP.append("Tujuan\t: "+ self.tujuan)
                self.tampilanTiket01PNP.append("Harga\t: Rp. "+str(Harga[0]))
                self.tampilanTiket01PNP.append("Harga Total\t: Rp. "+ str(Harga[0]*1))
            elif self.asal == 'Surabaya' and self.tujuan == 'Banyuwangi':
                self.tampilanTiket01PNP.append("Asal\t: " + self.asal)
                self.tampilanTiket01PNP.append("Tujuan\t: " + self.tujuan)
                self.tampilanTiket01PNP.append("Harga\t: Rp. " + str(Harga[1]))
                self.tampilanTiket01PNP.append("Harga Total\t: Rp. " + str(Harga[1] * 1))
            elif self.asal == 'Banyuwangi' and self.tujuan == 'Surabaya':
                self.tampilanTiket01PNP.append("Asal\t: " + self.asal)
                self.tampilanTiket01PNP.append("Tujuan\t: " + self.tujuan)
                self.tampilanTiket01PNP.append("Harga\t: Rp. " + str(Harga[1]))
                self.tampilanTiket01PNP.append("Harga Total\t: Rp. " + str(Harga[1] * 1))
            elif self.asal == 'Solo' and self.tujuan == 'Banyuwangi':
                self.tampilanTiket01PNP.append("Asal\t: " + self.asal)
                self.tampilanTiket01PNP.append("Tujuan\t: " + self.tujuan)
                self.tampilanTiket01PNP.append("Harga\t: Rp. " + str(Harga[2]))
                self.tampilanTiket01PNP.append("Harga Total\t: Rp. " + str(Harga[2] * 1))
            elif self.asal == 'Banyuwangi' and self.tujuan == 'Solo':
                self.tampilanTiket01PNP.append("Asal\t: " + self.asal)
                self.tampilanTiket01PNP.append("Tujuan\t: " + self.tujuan)
                self.tampilanTiket01PNP.append("Harga\t: Rp. " + str(Harga[2]))
                self.tampilanTiket01PNP.append("Harga Total\t: Rp. " + str(Harga[2] * 1))
            else:
                self.tampilanTiket01PNP.append("Mohon masukkan asal dan tujuan dengan benar")
        elif self.selection == jmlPenumpangDrop[1]: #Untuk 2 Penumpang
            self.asal, self.tujuan = self.asalcb02PNP.currentText(), self.tujuancb02PNP.currentText()
            self.nama02PNPA = self.namatxtLineEdit02PNPA.text()
            self.nama02PNPB = self.namatxtLineEdit02PNPB.text()
            self.tampilanTiket02PNP.clear()
            self.tampilanTiket02PNP.append("Tiket untuk "+ jmlPenumpangDrop[1]+" Penumpang")
            self.tampilanTiket02PNP.append("\n<html><u>Penumpang 01</u></html>")
            self.tampilanTiket02PNP.append("Nama\t: "+ self.nama02PNPA)
            self.tampilanTiket02PNP.append("<html><u>Penumpang 02</u></html>")
            self.tampilanTiket02PNP.append("Nama\t: " + self.nama02PNPB)
            self.tampilanTiket02PNP.append("\n<html><u><b>Asal Kota, Tujuan Kota, Harga Tiket:</b></u></html>")
            if self.asal == 'Surabaya' and self.tujuan == 'Solo':
                self.tampilanTiket02PNP.append("Asal\t: "+ self.asal)
                self.tampilanTiket02PNP.append("Tujuan\t: "+ self.tujuan)
                self.tampilanTiket02PNP.append("Harga\t: Rp. "+ str(Harga[0]))
                self.tampilanTiket02PNP.append("Harga Total\t: Rp. " + str(Harga[0]*2))
            elif self.asal == 'Solo' and self.tujuan == 'Surabaya':
                self.tampilanTiket02PNP.append("Asal\t: "+ self.asal)
                self.tampilanTiket02PNP.append("Tujuan\t: "+ self.tujuan)
                self.tampilanTiket02PNP.append("Harga\t: Rp. "+str(Harga[0]))
                self.tampilanTiket02PNP.append("Harga Total\t: Rp. "+ str(Harga[0]*2))
            elif self.asal == 'Surabaya' and self.tujuan == 'Banyuwangi':
                self.tampilanTiket02PNP.append("Asal\t: " + self.asal)
                self.tampilanTiket02PNP.append("Tujuan\t: " + self.tujuan)
                self.tampilanTiket02PNP.append("Harga\t: Rp. " + str(Harga[1]))
                self.tampilanTiket02PNP.append("Harga Total\t: Rp. " + str(Harga[1] * 2))
            elif self.asal == 'Banyuwangi' and self.tujuan == 'Surabaya':
                self.tampilanTiket02PNP.append("Asal\t: " + self.asal)
                self.tampilanTiket02PNP.append("Tujuan\t: " + self.tujuan)
                self.tampilanTiket02PNP.append("Harga\t: Rp. " + str(Harga[1]))
                self.tampilanTiket02PNP.append("Harga Total\t: Rp. " + str(Harga[1] * 2))
            elif self.asal == 'Solo' and self.tujuan == 'Banyuwangi':
                self.tampilanTiket02PNP.append("Asal\t: " + self.asal)
                self.tampilanTiket02PNP.append("Tujuan\t: " + self.tujuan)
                self.tampilanTiket02PNP.append("Harga\t: Rp. " + str(Harga[2]))
                self.tampilanTiket02PNP.append("Harga Total\t: Rp. " + str(Harga[2] * 2))
            elif self.asal == 'Banyuwangi' and self.tujuan == 'Solo':
                self.tampilanTiket02PNP.append("Asal\t: " + self.asal)
                self.tampilanTiket02PNP.append("Tujuan\t: " + self.tujuan)
                self.tampilanTiket02PNP.append("Harga\t: Rp. " + str(Harga[2]))
                self.tampilanTiket02PNP.append("Harga Total\t: Rp. " + str(Harga[2] * 2))
            else:
                self.tampilanTiket02PNP.append("Mohon masukkan asal dan tujuan dengan benar")
        elif self.selection == jmlPenumpangDrop[2]: #Untuk 3 Penumpang
            self.asal, self.tujuan = self.asalcb03PNP.currentText(), self.tujuancb03PNP.currentText()
            self.nama03PNPA = self.namatxtLineEdit03PNPA.text()
            self.nama03PNPB = self.namatxtLineEdit03PNPB.text()
            self.nama03PNPC = self.namatxtLineEdit03PNPC.text()
            self.tampilanTiket03PNP.clear()
            self.tampilanTiket03PNP.append("Tiket untuk " + jmlPenumpangDrop[2] + " Penumpang")
            self.tampilanTiket03PNP.append("\n<html><u>Penumpang 01</u></html>")
            self.tampilanTiket03PNP.append("Nama\t: " + self.nama03PNPA)
            self.tampilanTiket03PNP.append("<html><u>Penumpang 02</u></html>")
            self.tampilanTiket03PNP.append("Nama\t: " + self.nama03PNPB)
            self.tampilanTiket03PNP.append("<html><u>Penumpang 03</u></html>")
            self.tampilanTiket03PNP.append("Nama\t: " + self.nama03PNPC)
            self.tampilanTiket03PNP.append("\n<html><u><b>Asal Kota, Tujuan Kota, Harga Tiket:</b></u></html>")
            if self.asal == 'Surabaya' and self.tujuan == 'Solo':
                self.tampilanTiket03PNP.append("Asal\t: " + self.asal)
                self.tampilanTiket03PNP.append("Tujuan\t: " + self.tujuan)
                self.tampilanTiket03PNP.append("Harga\t: Rp. " + str(Harga[0]))
                self.tampilanTiket03PNP.append("Harga Total\t: Rp. " + str(Harga[0] * 2))
            elif self.asal == 'Solo' and self.tujuan == 'Surabaya':
                self.tampilanTiket03PNP.append("Asal\t: " + self.asal)
                self.tampilanTiket03PNP.append("Tujuan\t: " + self.tujuan)
                self.tampilanTiket03PNP.append("Harga\t: Rp. " + str(Harga[0]))
                self.tampilanTiket03PNP.append("Harga Total\t: Rp. " + str(Harga[0] * 2))
            elif self.asal == 'Surabaya' and self.tujuan == 'Banyuwangi':
                self.tampilanTiket03PNP.append("Asal\t: " + self.asal)
                self.tampilanTiket03PNP.append("Tujuan\t: " + self.tujuan)
                self.tampilanTiket03PNP.append("Harga\t: Rp. " + str(Harga[1]))
                self.tampilanTiket03PNP.append("Harga Total\t: Rp. " + str(Harga[1] * 2))
            elif self.asal == 'Banyuwangi' and self.tujuan == 'Surabaya':
                self.tampilanTiket03PNP.append("Asal\t: " + self.asal)
                self.tampilanTiket03PNP.append("Tujuan\t: " + self.tujuan)
                self.tampilanTiket03PNP.append("Harga\t: Rp. " + str(Harga[1]))
                self.tampilanTiket03PNP.append("Harga Total\t: Rp. " + str(Harga[1] * 2))
            elif self.asal == 'Solo' and self.tujuan == 'Banyuwangi':
                self.tampilanTiket03PNP.append("Asal\t: " + self.asal)
                self.tampilanTiket03PNP.append("Tujuan\t: " + self.tujuan)
                self.tampilanTiket03PNP.append("Harga\t: Rp. " + str(Harga[2]))
                self.tampilanTiket03PNP.append("Harga Total\t: Rp. " + str(Harga[2] * 2))
            elif self.asal == 'Banyuwangi' and self.tujuan == 'Solo':
                self.tampilanTiket03PNP.append("Asal\t: " + self.asal)
                self.tampilanTiket03PNP.append("Tujuan\t: " + self.tujuan)
                self.tampilanTiket03PNP.append("Harga\t: Rp. " + str(Harga[2]))
                self.tampilanTiket03PNP.append("Harga Total\t: Rp. " + str(Harga[2] * 2))
            else:
                self.tampilanTiket03PNP.append("Mohon masukkan asal dan tujuan dengan benar")
        elif self.selection == jmlPenumpangDrop[3]: #Untuk 4 Penumpang
            self.asal, self.tujuan = self.asalcb04PNP.currentText(), self.tujuancb04PNP.currentText()
            self.nama04PNPA = self.namatxtLineEdit04PNPA.text()
            self.nama04PNPB = self.namatxtLineEdit04PNPB.text()
            self.nama04PNPC = self.namatxtLineEdit04PNPC.text()
            self.nama04PNPD = self.namatxtLineEdit04PNPD.text()
            self.tampilanTiket04PNP.clear()
            self.tampilanTiket04PNP.append("Tiket untuk " + jmlPenumpangDrop[2] + " Penumpang")
            self.tampilanTiket04PNP.append("\n<html><u>Penumpang 01</u></html>")
            self.tampilanTiket04PNP.append("Nama\t: " + self.nama04PNPA)
            self.tampilanTiket04PNP.append("<html><u>Penumpang 02</u></html>")
            self.tampilanTiket04PNP.append("Nama\t: " + self.nama04PNPB)
            self.tampilanTiket04PNP.append("<html><u>Penumpang 03</u></html>")
            self.tampilanTiket04PNP.append("Nama\t: " + self.nama04PNPC)
            self.tampilanTiket04PNP.append("<html><u>Penumpang 03</u></html>")
            self.tampilanTiket04PNP.append("Nama\t: " + self.nama04PNPD)
            self.tampilanTiket04PNP.append("\n<html><u><b>Asal Kota, Tujuan Kota, Harga Tiket:</b></u></html>")
            if self.asal == 'Surabaya' and self.tujuan == 'Solo':
                self.tampilanTiket04PNP.append("Asal\t: " + self.asal)
                self.tampilanTiket04PNP.append("Tujuan\t: " + self.tujuan)
                self.tampilanTiket04PNP.append("Harga\t: Rp. " + str(Harga[0]))
                self.tampilanTiket04PNP.append("Harga Total\t: Rp. " + str(Harga[0] * 2))
            elif self.asal == 'Solo' and self.tujuan == 'Surabaya':
                self.tampilanTiket04PNP.append("Asal\t: " + self.asal)
                self.tampilanTiket04PNP.append("Tujuan\t: " + self.tujuan)
                self.tampilanTiket04PNP.append("Harga\t: Rp. " + str(Harga[0]))
                self.tampilanTiket04PNP.append("Harga Total\t: Rp. " + str(Harga[0] * 2))
            elif self.asal == 'Surabaya' and self.tujuan == 'Banyuwangi':
                self.tampilanTiket04PNP.append("Asal\t: " + self.asal)
                self.tampilanTiket04PNP.append("Tujuan\t: " + self.tujuan)
                self.tampilanTiket04PNP.append("Harga\t: Rp. " + str(Harga[1]))
                self.tampilanTiket04PNP.append("Harga Total\t: Rp. " + str(Harga[1] * 2))
            elif self.asal == 'Banyuwangi' and self.tujuan == 'Surabaya':
                self.tampilanTiket04PNP.append("Asal\t: " + self.asal)
                self.tampilanTiket04PNP.append("Tujuan\t: " + self.tujuan)
                self.tampilanTiket04PNP.append("Harga\t: Rp. " + str(Harga[1]))
                self.tampilanTiket04PNP.append("Harga Total\t: Rp. " + str(Harga[1] * 2))
            elif self.asal == 'Solo' and self.tujuan == 'Banyuwangi':
                self.tampilanTiket04PNP.append("Asal\t: " + self.asal)
                self.tampilanTiket04PNP.append("Tujuan\t: " + self.tujuan)
                self.tampilanTiket04PNP.append("Harga\t: Rp. " + str(Harga[2]))
                self.tampilanTiket04PNP.append("Harga Total\t: Rp. " + str(Harga[2] * 2))
            elif self.asal == 'Banyuwangi' and self.tujuan == 'Solo':
                self.tampilanTiket04PNP.append("Asal\t: " + self.asal)
                self.tampilanTiket04PNP.append("Tujuan\t: " + self.tujuan)
                self.tampilanTiket04PNP.append("Harga\t: Rp. " + str(Harga[2]))
                self.tampilanTiket04PNP.append("Harga Total\t: Rp. " + str(Harga[2] * 2))
            else:
                self.tampilanTiket04PNP.append("Mohon masukkan asal dan tujuan dengan benar")
        else:
            print("belum selesai bung")


    def btnCetakClicked(self):
        if self.selection == jmlPenumpangDrop[0]:
            dialog = QPrintPreviewDialog()
            dialog.paintRequested.connect(self.tampilanTiket01PNP.print_)
            dialog.exec_()
        elif self.selection == jmlPenumpangDrop[1]:
            dialog = QPrintPreviewDialog()
            dialog.paintRequested.connect(self.tampilanTiket02PNP.print_)
            dialog.exec_()
        elif self.selection == jmlPenumpangDrop[2]:
            dialog = QPrintPreviewDialog()
            dialog.paintRequested.connect(self.tampilanTiket03PNP.print_)
            dialog.exec_()
        elif self.selection == jmlPenumpangDrop[3]:
            dialog = QPrintPreviewDialog()
            dialog.paintRequested.connect(self.tampilanTiket04PNP.print_)
            dialog.exec_()