import sys
from PyQt6.QtWidgets import (QApplication, QLabel,
QWidget,QLineEdit, QPushButton,QMessageBox,QCheckBox)
from PyQt6.QtGui import QFont, QPixmap

class Login(QWidget):
    

    def __init__(self):
        super().__init__()
        self.inicializarLogin()

    def inicializarLogin(self):
        self.setGeometry(100,100,350,250)
        self.setWindowTitle("LoginPage")
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        self.is_logged = False

        user_label = QLabel(self)
        user_label.setText("Usuario")
        user_label.setFont(QFont('Arial',10))
        user_label.move(20,54)

        self.user_input = QLineEdit(self)
        self.user_input.resize(250,24)
        self.user_input.move(90,50)
        
        pass_label = QLabel(self)
        pass_label.setText("Password")
        pass_label.setFont(QFont('Arial',10))
        pass_label.move(20,86)

        self.pass_input = QLineEdit(self)
        self.pass_input.resize(250,24)
        self.pass_input.setEchoMode(
            QLineEdit.EchoMode.Password
        )
        self.pass_input.move(90,82)

        self.check_view_password = QCheckBox(self)
        self.check_view_password.setText("Ver la contraseña")
        self.check_view_password.move (90,110)
        

if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    login = Login()
    sys.exit(app.exec())