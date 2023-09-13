import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget,QLabel


class VentanaVacia(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializarUI()
    
    def inicializarUI(self):
        self.setGeometry(100, 100,250,250)
        self.setWindowTitle("Hola test 1")
        print("Funciona")
        self.show()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaVacia()

    sys.exit(app.exec())