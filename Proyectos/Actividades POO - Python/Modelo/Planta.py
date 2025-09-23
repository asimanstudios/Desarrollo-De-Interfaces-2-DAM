from abc import ABC, abstractmethod

class Planta(ABC):
    def __init__(self, nombre:str, altura:int, precio: float):
        self._nombre = nombre
        self._altura = self.validarAltura(altura)
        self._precio = self.validarPrecio(precio)
@staticmethod
def validarAltura(altura: int):
    if altura<5 or altura>300:
        raise ValueError("La altúra es inválida.")
    return altura
@staticmethod
def validarPrecio (precio: float):
    if precio<0:
        raise ValueError("Error: Precio negativo no aceptado")
    return precio
@abstractmethod
def getDescripcion(self) -> str:
    pass

