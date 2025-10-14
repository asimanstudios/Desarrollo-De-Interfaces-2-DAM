import sys
from PySide6.QtWidgets import QApplication
from ventana import Ventana

if __name__ == "__main__":
    app = QApplication([])
    #app = QApplication(sys.argv)
    # Crear una instancia de la ventana
    ventana = Ventana()
    ventana.show()
    # Ejecutar el bucle de eventos
    sys.exit(app.exec())
