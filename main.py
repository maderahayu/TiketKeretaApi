import sys
from PyQt5.QtWidgets import QApplication
from homeScreen import *

app = QApplication(sys.argv)
home = homeScreen()
home.show()

sys.exit(app.exec())
