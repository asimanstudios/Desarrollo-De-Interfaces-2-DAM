from Vista.Consola import Consola
class ControladorVivero():
    def iniciar():
        seleccion:0
        Consola.menu()
        if seleccion==1:
            ServiciosViviero.add()
        elif seleccion==2:
            ServiciosVivero.remove()
        elif seleccion==3:
            ServiciosVivero.edit()
        else:
            Consola.mensajeError("Seleccion Invalida")


        