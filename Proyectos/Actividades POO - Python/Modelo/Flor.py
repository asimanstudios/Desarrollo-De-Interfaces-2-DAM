from .Planta import Planta

class Flor(Planta):
    def __init__(self, nombre: str, altura: int, precio: float, color: str):
        super().__init__(nombre, altura, precio)
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    def getDescripcion(self) -> str:
        return f"Flor {self._color}"
