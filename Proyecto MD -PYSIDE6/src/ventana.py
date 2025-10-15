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
        # Cuando se hace click al boton se hace un print
        print("ILLO!!! Botón clicado!")
