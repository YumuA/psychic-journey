from PyQt6.QtWidgets import (QDialog, QLabel, QPushButton, QLineEdit,QMessageBox, QWidget)
from PyQt6.QtGui import QFont
import conexion

class Register_User_View(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        super().__init__()
        self.generar_formulario()

    def generar_formulario(self):
        self.setGeometry(100,100,350,250)
        self.setWindowTitle("Register Form Window")

        user_label = QLabel(self)
        user_label.setText("Usuario")
        user_label.setFont(QFont("Arial",11))
        user_label.move(20,50)

        self.user_input = QLineEdit(self)
        self.user_input.resize(150,24)
        self.user_input.move(170,50)

        pass_label1 = QLabel(self)
        pass_label1.setText("Contraseña")
        pass_label1.setFont(QFont("Arial",11))
        pass_label1.move(20,74)
        pass_label1.resize(150,24)
        
        self.pass_input1 = QLineEdit(self)
        self.pass_input1.resize(150,24)
        self.pass_input1.move(170, 74)
        self.pass_input1.setEchoMode(
            QLineEdit.EchoMode.Password
            )
        pass_label2 = QLabel(self)
        pass_label2.setText("Contraseña")
        pass_label2.setFont(QFont("Arial",11))
        pass_label2.move(20,100)
        pass_label2.resize(150,24)

        self.pass_input2 = QLineEdit(self)
        self.pass_input2.resize(150,24)
        self.pass_input2.move(170, 100)
        self.pass_input2.setEchoMode(
            QLineEdit.EchoMode.Password
            )

        createButton = QPushButton(self)
        createButton.setText("Crear Usuario")
        createButton.setFont(QFont("Arial",11))
        createButton.resize(150,32)
        createButton.move(20, 150)
        createButton.clicked.connect(self.crear_usuario)

        cancelButton = QPushButton(self)
        cancelButton.setText("Cancelar")
        cancelButton.setFont(QFont("Arial",11))
        cancelButton.resize(150,32)
        cancelButton.move(170, 150)
        cancelButton.clicked.connect(self.cancelar_creacion)

    def cancelar_creacion(self):
        self.Close()

    def crear_usuario(self):
        usr_path = 'usuarios.txt'
        usuario1 = self.user_input.text()

        passw1 = self.pass_input1.text()
        passw12 = self.pass_input2.text()
        
        if passw1 == '' or passw12 == '' or usuario1 == '':
            QMessageBox.warning(self, "Pirobo tonto",
                                f"Todo Vacio",
                                QMessageBox.StandardButton.Close)
        elif passw1 != passw12:
            QMessageBox.warning(self, "Pirobo tonto no son iguales las contraseñas",
                                f"todo tonto",
                                QMessageBox.StandardButton.Close)
        else:
            try:
                with open(usr_path, 'a+') as f:
                    f.write(f"{usuario1},{passw1}\n")
                QMessageBox.information(self, 'Creado correctamente',
                                        f"asd",
                                        QMessageBox.StandardButton.Ok)

            except FileNotFoundError as e:
                        QMessageBox.warning(self, f"No se encontró el archivo: {e}", 
                                            f"as",
                        QMessageBox.StandardButton.Close)

                