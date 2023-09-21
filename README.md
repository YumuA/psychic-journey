# Proyecto de Modelamiento de Base de Datos

Este proyecto es una implementación de una base de datos para el registro de músicos, obras famosas e instrumentos musicales. La base de datos permite almacenar información sobre músicos, obras en las que participan y los instrumentos utilizados en esas obras. El proyecto incluye una interfaz gráfica desarrollada en Python para interactuar con la base de datos.

## Integrantes del Equipo

- [Kevin Santiago Rojas]
- [Juan Manuel Leyva]

## Profesor

- Profesor: Elkin Arévalo

## Contenido

- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura de la Base de Datos](#estructura-de-la-base-de-datos)
- [Funcionalidades](#funcionalidades)
- [Capturas de Pantalla](#capturas-de-pantalla)
- [Licencia](#licencia)

## Requisitos

- Python 3.x
- Oracle Database (se asume que se tiene una base de datos Oracle instalada y configurada)

## Instalación
    
1. Clona el repositorio en tu máquina local:

```bash
git clone https://github.com/tu-usuario/tu-proyecto.git

pip install cx_Oracle
pip install tkinter
pip install ttkthemes

```

## USO 
-Asegúrate de tener una base de datos Oracle configurada y accesible.
-Ejecuta la aplicación Python:

```bash
    python main.py

```
## Estructura de la Base de Datos

# La base de datos está diseñada con las siguientes tablas:

Musico: Almacena información sobre los músicos, incluyendo su nombre, fecha de nacimiento y fecha de muerte (si aplica).
ObraFamosa: Contiene detalles sobre obras famosas, como su nombre.
InstrumentoMusical: Registra información sobre instrumentos musicales, incluyendo nombre, lugar de creación, creador, tipo y materiales.
MusicoObraFamosa: Esta tabla representa la relación entre músicos y obras famosas, indicando qué músicos participaron en qué obras.
InstrumentoObraFamosa: Esta tabla representa la relación entre instrumentos y obras famosas, indicando qué instrumentos se utilizaron en qué obras.

## Funcionalidades
# El proyecto ofrece las siguientes funcionalidades:

Agregar, buscar y eliminar músicos.
Consultar obras y ver los músicos que participaron en ellas.
Consultar instrumentos y ver las obras en las que se utilizaron.
Ver detalles de un músico, obra o instrumento, incluyendo las obras relacionadas.
Capturas de Pantalla
Captura de pantalla 1
Captura de pantalla 2
