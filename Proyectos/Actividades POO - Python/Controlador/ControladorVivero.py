from Servicio.ServiciosViviero import ViveroVillanueva
from Vista.Consola import Consola

class ControladorVivero:
    def __init__(self):
        self.servicio = ViveroVillanueva()

    def iniciar(self):
        Consola.ejecucionMenu(self)

        