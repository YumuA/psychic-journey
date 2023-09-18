import sys
import cx_Oracle
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLabel, QPushButton, QLineEdit
from PyQt6.QtCore import Qt 

class DatabaseConnection:
    def __init__(self):
        # Parámetros de conexión a la base de datos
        self.usuario = 'C##Ssant'
        self.contraseña = '1013'
        self.dsn = 'localhost:1521/XE'
        self.connection = None  # Inicialmente, la conexión está en None

    def conectar(self):
        try:
            # Establece la conexión a la base de datos usando los parámetros
            self.connection = cx_Oracle.connect(
                user=self.usuario,
                password=self.contraseña,
                dsn=self.dsn
            )
        except cx_Oracle.Error as error:
            print(f"Error de Oracle al conectar: {error}")

    def desconectar(self):
        if self.connection:
            # Si hay una conexión existente, ciérrala
            self.connection.close()
            self.connection = None  # Restablece la conexión a None después de cerrarla
class ConsultasApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Consulta de Base de Datos")
        self.setGeometry(100, 100, 800, 400)

        layout = QVBoxLayout()

        self.db = DatabaseConnection()
        self.db.conectar()

        self.combo = QComboBox()
        self.combo.addItem("Ver Músicos")
        self.combo.addItem("Ver Obras Famosas")
        self.combo.addItem("Ver Instrumentos")
        self.combo.addItem("Ver a los músicos y sus obras famosas")
        self.combo.addItem("Ver a los musicos que participaron en obras famosas")

        self.where_input = QLineEdit()  # Agrega un campo de entrada para la cláusula WHERE
        self.where_input.setPlaceholderText("Ingresa una cláusula WHERE")
        
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        self.label.setWordWrap(True)

        self.boton_consultar = QPushButton("Consultar")
        self.boton_consultar.clicked.connect(self.realizar_consulta)

        layout.addWidget(self.combo)
        layout.addWidget(self.where_input)  # Agrega el campo de entrada WHERE
        layout.addWidget(self.label) # Salida de la información
        layout.addWidget(self.boton_consultar) 

        self.setLayout(layout)


    def realizar_consulta(self):
        opcion = self.combo.currentText()

        if opcion == "Ver Músicos":
            # Consulta para músicos
            cursor = self.db.connection.cursor()
            cursor.execute('SELECT nombre FROM musico')
            result = cursor.fetchall()
            cursor.close()
            self.label.setText("\n".join([row[0] for row in result]))

        elif opcion == "Ver Obras Famosas":
            # Consulta para obras famosas
            cursor = self.db.connection.cursor()
            cursor.execute('SELECT * FROM obrafamosa')
            result = cursor.fetchall()
            cursor.close()
            self.label.setText("\n".join([str(row) for row in result]))

        elif opcion == "Ver Instrumentos":
            # Consulta para instrumentos
            cursor = self.db.connection.cursor()
            cursor.execute('SELECT * FROM instrumentomusical')
            result = cursor.fetchall()
            cursor.close()
            self.label.setText("\n".join([str(row) for row in result]))

        elif opcion == "Ver a los músicos y sus obras famosas":
            # Consulta personalizada con WHERE
            self.where_input.setPlaceholderText("Ingresa por nombre del musico")
            where_clause = self.where_input.text().strip()  # Eliminar espacios en blanco
            cursor = self.db.connection.cursor()
            
            if not where_clause:
                # Si la cláusula WHERE está vacía, ejecuta la consulta sin ella
                cursor.execute('''SELECT M.nombre, o.nombre 
                                FROM Musico M
                                JOIN musicoobrafamosa m ON m.musicoid = M.musicoid
                                JOIN obrafamosa o ON m.obraid = o.obraid''')
            else:
                cursor.execute(f'''SELECT M.nombre, o.nombre 
                                FROM Musico M
                                JOIN musicoobrafamosa m ON m.musicoid = M.musicoid
                                JOIN obrafamosa o ON m.obraid = o.obraid
                                WHERE M.nombre = '{where_clause}' ''') 
                result = cursor.fetchall()
                cursor.close()
                self.label.setText("\n".join([str(row) for row in result]))

        elif opcion == 'Ver a los musicos que participaron en obras famosas':
            # Si tiene un parametro
            where_clause = self.where_input.text()
            cursor = self.db.connection.cursor()
            cursor.execute(f'''SELECT o.nombre AS nombre_obra, LISTAGG(M.nombre, ', ') WITHIN GROUP (ORDER BY M.nombre) AS nombres_musicos
                            FROM Musico M
                            JOIN musicoobrafamosa m ON m.musicoid = M.musicoid
                            JOIN obrafamosa o ON m.obraid = o.obraid
                            WHERE o.nombre  = '{where_clause}'
                            GROUP BY o.nombre
                            ORDER BY nombre_obra
                            ''')
            result = cursor.fetchall()
            cursor.close()
            self.label.setText("\n".join([str(row) for row in result]))

def closeEvent(self, event):
    self.db.desconectar()


    def closeEvent(self, event):
        self.db.desconectar()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConsultasApp()
    window.show()
    sys.exit(app.exec())
