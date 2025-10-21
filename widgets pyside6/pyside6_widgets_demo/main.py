from PySide6 import QtWidgets, QApplication
from widgets import ( checkbox,combobox,datetimeedit,dial,groupbox,label,lineedit,pushbutton,radiobuttons,slider,tablewidget,tabwidget,textedit )

if __name__ == "__main__":
    import  sys 
    from demoWindow import DemoWindow
    app = QApplication(sys.argv) #cargar app

    window = DemoWindow()
    window.show()
    sys.exit(app.exec())
