from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QBoxLayout
from .label import create as create_label

class DemoWindow(QMainWindow): # hereda de qmainwindow
# zona declarativa
    central_widget: QWidget = None
    main_layout: QBoxLayout = None
    widgets: dict = {}

    def __init__(self): #constructor
        super().__init__()
        #configurar la ventana
        self.setWindowTitle("DemoWindow con Pyside6")
        #tamaño
        self.resize(600,900)
        #widget de la ventana
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # layout
        self.main_layout = QBoxLayout(QBoxLayout.TopToBottom, self.central_widget) #  self.main_layout = QBoxLayout(self.central_widget)

        self.refs = ()
        self.add_label()

    def add_label(self):
        box, exposed = create_label(self.central_widget)
        self.main_layout.addWidget(box)
        self.widgets["label"] = exposed
