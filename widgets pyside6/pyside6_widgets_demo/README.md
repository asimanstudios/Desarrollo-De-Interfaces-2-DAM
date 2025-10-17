
# Demo de Widgets PySide6 (modular, POO)

Este proyecto muestra una **ventana principal** que incorpora, mediante **métodos separados** (y módulos separados), los siguientes widgets de PySide6:

- QCheckBox
- QLabel
- QGroupBox
- QComboBox
- QRadioButton
- QPushButton
- QTabWidget
- QTableWidget
- QLineEdit
- QTextEdit
- QDateTimeEdit
- QSlider
- QDial

Cada widget se implementa en un **módulo** dentro de `widgets/` con una función `create(parent=None)` que devuelve una tupla `(groupbox, exposed)`:
- `groupbox`: un `QGroupBox` listo para añadirse a un layout.
- `exposed`: un diccionario con referencias a controles relevantes (por ejemplo, `{"slider": QSlider}`), útil para sincronizar widgets (p. ej. `QDial` y `QSlider`).

## Requisitos

- Python 3.9+ (recomendado)
- PySide6

Instalación de dependencias:
```bash
pip install -r requirements.txt
```

## Ejecutar la demo

```bash
python main.py
```

## Estructura

```
pyside6_widgets_demo/
├── main.py
├── requirements.txt
├── README.md
└── widgets/
    ├── __init__.py
    ├── checkbox.py
    ├── label.py
    ├── groupbox.py
    ├── combobox.py
    ├── radiobuttons.py
    ├── pushbutton.py
    ├── tabwidget.py
    ├── tablewidget.py
    ├── lineedit.py
    ├── textedit.py
    ├── datetimeedit.py
    ├── slider.py
    └── dial.py
```

## Notas didácticas

- Señales clave conectadas a `print()` para observar el flujo de eventos en la consola.
- `QDial` y `QSlider` están **sincronizados** en `main.py` como ejemplo de interacción entre widgets.
