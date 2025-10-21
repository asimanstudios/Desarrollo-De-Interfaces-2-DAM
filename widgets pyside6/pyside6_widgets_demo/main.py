from PySide6.QtWidgets import QApplication
from widgets import ( checkbox,combobox,datetimeedit,dial,groupbox,label,lineedit,pushbutton,radiobuttons,slider,tablewidget,tabwidget,textedit,demoWindow )

if __name__ == "__main__":
    import  sys
    app = QApplication(sys.argv) #cargar app

    window = demoWindow.DemoWindow()
    window.show()
    sys.exit(app.exec())
