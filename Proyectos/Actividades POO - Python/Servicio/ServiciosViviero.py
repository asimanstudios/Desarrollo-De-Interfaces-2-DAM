from typing import List
from Modelo.Planta import Planta, PlantaException
from Modelo.Cactus import Cactus
from Modelo.Flor import Flor
from Modelo.ViveroInterface import ViveroInterface

class ViveroVillanueva(ViveroInterface):
    def __init__(self):
        self._plantas: List[Planta] = []

    def agregarCactus(self, nombre: str, altura: int, precio: float, tieneEspinas: bool) -> Planta:
        cactus = Cactus(nombre, altura, precio, tieneEspinas)
        self._plantas.append(cactus)
        return cactus

    def agregarFlor(self, nombre: str, altura: int, precio: float, color: str) -> Planta:
        flor = Flor(nombre, altura, precio, color)
        self._plantas.append(flor)
        return flor

    def buscarPlanta(self, nombre: str) -> Planta | None:
        for planta in self._plantas:
            if planta.nombre == nombre:
                return planta
        return None

    def modificarPrecioPlanta(self, nombre: str, precio: float) -> Planta | None:
        planta = self.buscarPlanta(nombre)
        if planta:
            try:
                planta.precio = precio
            except PlantaException:
                pass  
            return planta
        return None

    def eliminarPrimeraPlantaConNombre(self, nombre: str) -> Planta:
        for i, planta in enumerate(self._plantas):
            if planta.nombre == nombre:
                return self._plantas.pop(i)
        raise PlantaException(f"No se encontró ninguna planta con el nombre '{nombre}'")

    def listarPlantas(self) -> List[Planta]:
        return self._plantas.copy()

    def buscarPorAlturaEntre(self, alturaMin: int, alturaMax: int) -> List[Planta]:
        return [p for p in self._plantas if alturaMin <= p.altura <= alturaMax]

    def buscarPorPrecioMenorA(self, precio: float) -> List[Planta]:
        return [p for p in self._plantas if p.precio <= precio]
    
