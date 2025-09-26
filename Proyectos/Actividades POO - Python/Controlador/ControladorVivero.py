from ..Servicio.ServiciosViviero import ServiciosViviero
from ..Vista.Consola import Consola

class ControladorVivero:
    def __init__(self):
        self.servicio = ServiciosViviero()

    def iniciar(self):
        Consola.ejecucionMenu(self)

        