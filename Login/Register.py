from PyQt6.QtWidgets import (QDialog, QLabel, QPushButton, QLineEdit,QMessageBox, QWidget)
from PyQt6.QtGui import QFont

class Register_User_View(QDialog):
    def __init__(self):
        self.setModal(True)
        super().__init__()
        self.generar_formulario()

    def generar_formulario(self):
        self.setGeometry(100,100,350,250)
        self.setWindowTitle("Register Form Window")

        user_label = QLabel(self)
        user_label.setText("Usuario")
        user_label.setFont(QFont("Arial",12))
        user_label.move(20,54)

        self.user_input = QLineEdit(self)
        self.user_input.resize(250,24)
        self.user_input.move(90,40)

        pass_label1 = QLabel(self)
        pass_label1.setText("Contraseña")
        pass_label1.move(20,74)
        pass_label1.resize(250,24)
        
        self.pass_input1 = QLineEdit(self)
        self.pass_input1.resize(250,24)
        self.pass_input1.move(90, 70)
        self.pass_input1.setEchoMode(
            QLineEdit.EchoMode.Password
            )
        pass_label2 = QLabel(self)
        pass_label2.setText("Confirma la Contraseña")
        pass_label2.move(20,100)
        pass_label2.resize(250,24)

        self.pass_input2 = QLineEdit(self)
        self.pass_input2.resize(250,24)
        self.pass_input2.move(90, 100)
        self.pass_input2.setEchoMode(
            QLineEdit.EchoMode.Password
            )