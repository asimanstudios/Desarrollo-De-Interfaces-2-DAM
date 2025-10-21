from PySide6.QtWidgets import QGroupBox, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

def create(parent=None):
    groupbox = QGroupBox("Ejemplo de QGroupBox", parent)
    layout = QVBoxLayout(groupbox)

    label = QLabel("Este es un ejemplo de contenido dentro de un QGroupBox.")
    label.setAlignment(Qt.AlignCenter)

    infoLabel = QLabel ("Selales - Ninguna | Metodos: getText(str), setAlignment(...)")
    infoLabel.setStyleSheet("color: gray; Font-Size: 10pt;")

    layout.addWidget(label)
    layout.addWidget(infoLabel)

    groupbox.setLayout(layout)

    exposed = {"label header": label,"infoLabel": infoLabel}
    return groupbox, exposed