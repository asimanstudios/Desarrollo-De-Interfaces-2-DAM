from abc import ABC, abstractmethod
from typing import List
from .Planta import Planta, PlantaException

class ViveroInterface(ABC):
    @abstractmethod
    def agregarCactus(self, nombre: str, altura: int, precio: float, tieneEspinas: bool) -> Planta:
        pass

    @abstractmethod
    def agregarFlor(self, nombre: str, altura: int, precio: float, color: str) -> Planta:
        pass

    @abstractmethod
    def buscarPlanta(self, nombre: str) -> Planta | None:
        pass

    @abstractmethod
    def modificarPrecioPlanta(self, nombre: str, precio: float) -> Planta | None:
        pass

    @abstractmethod
    def eliminarPrimeraPlantaConNombre(self, nombre: str) -> Planta:
        pass

    @abstractmethod
    def listarPlantas(self) -> List[Planta]:
        pass

    @abstractmethod
    def buscarPorAlturaEntre(self, alturaMin: int, alturaMax: int) -> List[Planta]:
        pass

    @abstractmethod
    def buscarPorPrecioMenorA(self, precio: float) -> List[Planta]:
        pass
