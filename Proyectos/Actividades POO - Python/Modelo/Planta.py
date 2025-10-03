from abc import ABC, abstractmethod
from .PlantaException import PlantaException

class Planta(ABC):
    def __init__(self, nombre: str, altura: int, precio: float):
        self._nombre = nombre
        self._altura = self.validarAltura(altura)
        self._precio = self.validarPrecio(precio)

    @staticmethod
    def validarAltura(altura: int) -> int:
        if not (5 <= altura <= 300):
            raise PlantaException("La altura debe estar entre 5 y 300 cm")
        return altura

    @staticmethod
    def validarPrecio(precio: float) -> float:
        if precio <= 0:
            raise PlantaException("El precio debe ser mayor que 0")
        return precio

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, value):
        self._altura = self.validarAltura(value)

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        self._precio = self.validarPrecio(value)

    @abstractmethod
    def getDescripcion(self) -> str:
        pass

