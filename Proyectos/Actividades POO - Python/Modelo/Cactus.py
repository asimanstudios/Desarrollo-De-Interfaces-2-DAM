from .Planta import Planta

class Cactus(Planta):
    def __init__(self, nombre: str, altura: int, precio: float, tieneEspinas: bool):
        super().__init__(nombre, altura, precio)
        self._tieneEspinas = tieneEspinas

    @property
    def tieneEspinas(self):
        return self._tieneEspinas

    @tieneEspinas.setter
    def tieneEspinas(self, value):
        self._tieneEspinas = value

    def getDescripcion(self) -> str:
        espinas = "con espinas" if self._tieneEspinas else "sin espinas"
        return f"Cactus {espinas}"
        