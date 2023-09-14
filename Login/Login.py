import sys
from PyQt6.QtWidgets import (QApplication, QLabel,
QWidget,QLineEdit, QPushButton,QMessageBox,QCheckBox, QVBoxLayout)
from PyQt6.QtGui import QFont, QPixmap 
import mysql.connector


class MainView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main View")
        self.setGeometry(100, 100, 350, 250)
        layout = QVBoxLayout()
        welcome_label = QLabel("¡Bienvenido a la vista principal!")
        layout.addWidget(welcome_label)
        self.setLayout(layout)

class Login(QWidget):
    
    print("El clase login iniciada...")

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
        self.check_view_password.toggled.connect(self.show_pass)

        login_button = QPushButton(self)
        login_button.setText("Login")
        login_button.setFont(QFont("Arial", 12))
        login_button.resize(120,40)
        login_button.move(90,140)
        login_button.clicked.connect(self.iniciar_sesion)


        register_button = QPushButton(self)
        register_button.setText("register")
        register_button.setFont(QFont("Arial", 12))
        register_button.resize(120,40)
        register_button.move(90,180)
        register_button.clicked.connect(self.registrar_usr)

    def show_pass(self, clicked):
        if clicked:
            self.pass_input.setEchoMode(
                QLineEdit.EchoMode.Normal
                )
        else:
            self.pass_input.setEchoMode(
                QLineEdit.EchoMode.Password
                )

    def iniciar(self):
        pass

    def registrar_usr(self):
        pass

    def iniciar_sesion(self):
        usuario = self.user_input.text()
        contraseña = self.pass_input.text()
        pass

        try:
            conexion = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password ='',
            database = 'test1'
        )
            if conexion.is_connected():
                cursor = conexion.cursor(dictionary=True)
                consulta = "SELECT * FROM usuarios WHERE usuario = %s AND contraseña = %s"
                cursor.execute(consulta, (usuario, contraseña))
                resultado = cursor.fetchone()


            if resultado:
                QMessageBox.information(self, "Exito", "Conectado Correctamente a MYSQL")
                self.is_logged = True
                conexion.close()

                self.main_view = MainView()
                self.main_view.show()
                self.hide()


            else:
              QMessageBox.warning(self, "Error", "No se pudo conectar a MySQL")
        except mysql.connector.Error as error:
            QMessageBox.warning(self, "Error", f'Error MYSQL {error}')


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    print("El inicio...")

    login = Login()
    sys.exit(app.exec())
    