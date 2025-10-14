# Mi primer Hola Mundo con PySide6

## Índice
- [Contexto](#contexto)
- [Objetivos de aprendizaje](#objetivos-de-aprendizaje)
- [Requisitos previos](#requisitos-previos)
- [Creación y activación del entorno virtual](#creación-y-activación-del-entorno-virtual)
- [Instalación de dependencias](#instalación-de-dependencias)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Código fuente](#código-fuente)
  - [ventana.py](#ventanapy)
  - [main.py](#mainpy)
- [Ejecución y prueba](#ejecución-y-prueba)
- [Cierre y siguientes pasos](#cierre-y-siguientes-pasos)
- [Checklist rápido del alumno](#checklist-rápido-del-alumno)

## Contexto
- En esta guía vamos a instalar y construir un proyecto de ventana básica con PySide6 a modo de interfaz gráfica.
- Usaremos 1 clase que almacenara el funcionamiento del programa y una clase principal para la ejecución
- Repositorio: [Link](https://github.com/asimanstudios/Desarrollo-De-Interfaces-2-DAM)

## Objetivos de aprendizaje
- Crear y activar un entorno virtual con python.
- Instalar dependencias con pip.
- Ejecutar una ventana básica con PySide6.
- Entender el rol de QApplication y el ciclo de eventos.
- Separar responsabilidades en el código de forma simple.

## Requisitos previos
- Python 3.11 (o superior).
- Sistema operativo: Windows 11.
- Herramientas: Git y Visual Studio Code.

## Creación y activación del entorno virtual

### Windows
> Para crear el entorno virtual debemos instalar virtual env en el equipo Windows

````cmd
python -m pip install virtualenv
````
>Tras esto deberemos crear **DENTRO** del directorio del proyecto el entorno virtual:
```cmd
#Crear el entorno virtual
python -m venv venv
#Iniciar el entorno virtual
.venv\Scripts\activate
```

Verificar la versión de Python y el intérprete activo:
```cmd
python --version
where python
```

## Instalación de dependencias
- Una vez dentro del entorno virtual tenemos que instalar unas dependencias que serán lo que nos permiten usar funciones y metodos para crear la interfaz gráfica
1. Instala PySide6:
```cmd
pip install PySide6
```

PySide6 es una librería que permite crear interfaces gráficas con Qt usando Python como lenguaje. Documentación oficial de PySide6: [PySide6 Docs](https://doc.qt.io/qtforpython/).

Generar el archivo requirements.txt:
- A la hora de transladar el proyecto es hutil e importante contar con las instalaciones de dependencias necesarias. Si las almacenamos en un fichero de texto podremos instalarlas posteriormente directamente con un comando. 
```cmd
#Almacenar dependencias
pip freeze > requirements.txt
#Instalar Dependencias:
pip install -r requirements.txt
```

## Estructura del Proyecto:
- Nuestro proyecto tendra la siguiente estructura *organizativa* de carpetas y ficheros.
```
proyecto-hola-mundo/
├─ src/
│  ├─ main.py          # Punto de entrada
│  └─ ventana.py       # Clase Ventana
├─ .gitignore
├─ requirements.txt
└─ README.md
```

Al dividir el codigo en metodos y en diferentes clases estamos modularizando y separando responsabilidades. Si en un futuro queremos reusar código podremos implementar clases ya creadas y a la hora de crear nuevos proyectos se facilitará el proceso enormemente ademas de que tendremos una estructura mas limpia, mas legible y mas mantenible por ende tenemos una clase ventana que es la que se encarga de crear la ventana gráfica y despues tenemos main que se encarga de arrancar el programa.


## Código fuente

### ventana.py
```python
# Importamos las clases necesarias de PySide6 para crear la ventana, etiqueta, layout y botón
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton

class Ventana(QWidget):  # Clase Ventana que hereda de QWidget (la base para ventanas)
    def __init__(self):  # Método que se ejecuta al crear la ventana
        super().__init__()  # Llama al constructor de la clase padre QWidget
        self.setWindowTitle("Hola Mundo usando PySide6")  # Título de la ventana
        self.setGeometry(100, 100, 300, 200)  # Posición (x, y) y tamaño (ancho, alto)

        # Crear un layout vertical para organizar los elementos uno debajo del otro
        layout = QVBoxLayout()

        # Crear una etiqueta (texto) con "Hola Mundo"
        texto = QLabel("Hola Mundo")
        layout.addWidget(texto)  # Añadir la etiqueta al layout

        # Crear un botón con texto "Haz clic aquí"
        boton = QPushButton("Haz clic aquí")
        # Conectar la señal 'clicked' del botón a la función 'on_button_clicked' (slot)
        # Esto significa: cuando se haga clic en el botón, se ejecutará esa función
        boton.clicked.connect(self.on_button_clicked)
        layout.addWidget(boton)  # Añadir el botón al layout

        # Aplicar el layout a la ventana
        self.setLayout(layout)

    def on_button_clicked(self):  # Función (slot) que responde al clic del botón
        """Esta función se ejecuta cada vez que se hace clic en el botón."""
        print("¡Botón clicado! Hola desde PySide6.")  # Imprime un mensaje en la consola
```
Un widget es un elemento de la interfaz, como una ventana o etiqueta y otros tipos. Se añaden a la ventana principal con una funcion para formar la UI o interfaz de usuario como si se almacenásen dentro de una lista.

### main.py
```python
import sys
#Importacion de clases de Pyside6
from PySide6.QtWidgets import QApplication
#Importamos la clase ventana que hemos creado antes.
from ventana import Ventana
#Si el nombre del fichero es main ejecutamos lo que hay debajo
if __name__ == "__main__":
    # Crear la instancia de QApplication para la ejecución de la interfaz
    app = QApplication([])
    # Crear una instancia de la ventana en base a la clase que hemos creado
    ventana = Ventana()
    #Mostrar la ventana en pantalla
    ventana.show()
    # Ejecutar el bucle de eventos de la aplicación
    sys.exit(app.exec())
```
- El bucle de eventos es muy importante ya que es lo que va a mantener por asi decirlo viva la aplicación, la va a actualizar y va a controlar las interacciones con la misma.
- QApplication maneja la aplicación como tal y el bucle de eventos procesa interacciones del usuario con la interfaz en si.

## Ejecución y prueba
- Para ejecutar la aplicacion debemos con el entorno virtual activo, ir a la carpeta src/ y ejecutar el siguiente comando:
```cmd
py main.py
```

Deberiamos ver una ventana con el título "Hola Mundo usando PySide6" y el texto "Hola Mundo" dentro de la ventana en si.

## Cierre y siguientes pasos:
1. Agregar boton:
- Se ha añadido un botón que captura clics usando señales y ranuras.
- El modelo de señales y ranuras permite conectar eventos (señales) a funciones (slots) que responden a los clicks o interacciones del usuario. 
- En este caso, el clic del botón imprime un mensaje en la consola pero se podria ejecutar cualquier funcion.
````python
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola Mundo usando PySide6")
        self.setGeometry(100, 100, 300, 200)
        # Crear un layout
        layout = QVBoxLayout()
        # Crear una etiqueta con el texto que se pide.
        texto = QLabel("Hola Mundo")
        # Agregar la etiqueta como widget al layout de la interfaz basicamente se agrega este item a la interfaz
        layout.addWidget(texto)
        # Crear un botón y conectar la señal clicked al slot
        #Crear el boton en cuestion con un texto
        boton = QPushButton("Boton")
        #Al hacer click en el boton se marca como clicado
        boton.clicked.connect(self.btn_clicado)  # Señal conectada al boton
        #Se agrega el boton a la interfaz
        layout.addWidget(boton)
        # Establecer el layout en la ventana
        self.setLayout(layout)

    def btn_clicado(self):
    # Cuando se hace click al boton se hace una escritura en la consola.
    print("ILLO!!! Botón clicado!")
````
2. Cierre del entorno:
- Una vez finalicemos con el entorno virtual es importante cerrarlo dado que si no se quedará corriendo en el ordenador consumiendo recursos.
- Para esto ejecutaremos un comando:
````cmd
#Se debe de hacer desde el directorio que almacena la carpeta venv.
.\venv\Scripts\deactivate
````
Se utiliza un layout vertical para posicionar automáticamente los widgets (etiqueta y botón) en lugar de coordenadas absolutas, facilitando la responsividad.

## Layout Vertical
Los layouts permiten organizar los widgets de manera automática y  de forma que sean responsivos, adaptándose al tamaño de la ventana sin tner que calcular posiciones manuales.
Por ejemplo, en lugar de usar `setGeometry()` para cada widget, un `QVBoxLayout` apila los elementos verticalmente y ajusta su tamaño automáticamente cuando la ventana cambia de tamaño.

## Checklist del alumno
- [x] He creado y activado el venv.
- [x] He instalado PySide6 y generado requirements.txt.
- [x] He separado main.py y ventana.py.
- [x] He incluido bloques de código con comentarios.
- [x] He explicado QApplication, widgets y app.exec().
- [x] He probado la app y documentado la ejecución.
