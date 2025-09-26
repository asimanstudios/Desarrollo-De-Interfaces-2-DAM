
from .Escaner import Escaner

class Consola:
    @staticmethod
    def menuConsola():
        print("===========VIVIEROS VILLANUEVA===========")
        print("1. Agregar planta")
        print("2. Eliminar planta")
        print("3. Modificar precio")
        print("4. Buscar planta")
        print("5. Listar plantas")
        print("6. Buscar por altura")
        print("7. Buscar por precio")
        print("8. Salir")

    @staticmethod
    def mensajeSalida():
        print("Saliendo!")

    @staticmethod
    def mensajeError(mensaje: str):
        print("Error:", mensaje)

    @staticmethod
    def pedirTipo() -> str:
        print("Indica el tipo de planta (planta/cactus/flor): ")
        return Escaner.pedirDato().lower()

    @staticmethod
    def pedirNombre() -> str:
        print("Indica el nombre de la planta: ")
        return Escaner.pedirDato()

    @staticmethod
    def pedirAltura() -> int:
        print("Indica la altura de la planta (cm): ")
        return int(Escaner.pedirDato())

    @staticmethod
    def pedirPrecio() -> float:
        print("Indica el precio de la planta: ")
        return float(Escaner.pedirDato())

    @staticmethod
    def pedirColor() -> str:
        print("Indica el color de la flor: ")
        return Escaner.pedirDato()

    @staticmethod
    def pedirEspinas() -> bool:
        print("¿La planta tiene espinas? (si/no): ")
        return Escaner.pedirDato().lower() == "si"

    @staticmethod
    def ejecucionMenu(controlador):
        while True:
            Consola.menuConsola()
            try:
                seleccion = int(Escaner.pedirDato())
                if seleccion == 1:
                    Consola.agregarPlanta(controlador)
                elif seleccion == 2:
                    Consola.eliminarPlanta(controlador)
                elif seleccion == 3:
                    Consola.modificarPrecio(controlador)
                elif seleccion == 4:
                    Consola.buscarPlanta(controlador)
                elif seleccion == 5:
                    Consola.listarPlantas(controlador)
                elif seleccion == 6:
                    Consola.buscarPorAltura(controlador)
                elif seleccion == 7:
                    Consola.buscarPorPrecio(controlador)
                elif seleccion == 8:
                    Consola.mensajeSalida()
                    break
                else:
                    Consola.mensajeError("Selección inválida")
            except ValueError:
                Consola.mensajeError("Entrada inválida")

    @staticmethod
    def agregarPlanta(controlador):
        tipo = Consola.pedirTipo()
        nombre = Consola.pedirNombre()
        altura = Consola.pedirAltura()
        precio = Consola.pedirPrecio()
        try:
            if tipo == "cactus":
                espinas = Consola.pedirEspinas()
                controlador.servicio.agregarCactus(nombre, altura, precio, espinas)
                print("Planta añadida")
            elif tipo == "flor":
                color = Consola.pedirColor()
                controlador.servicio.agregarFlor(nombre, altura, precio, color)
                print("Planta añadida")
            else:
                Consola.mensajeError("Tipo de planta no válido")
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def eliminarPlanta(controlador):
        nombre = Consola.pedirNombre()
        try:
            eliminada = controlador.servicio.eliminarPrimeraPlantaConNombre(nombre)
            print(f"Planta eliminada: {eliminada.getDescripcion()}")
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def modificarPrecio(controlador):
        nombre = Consola.pedirNombre()
        precio = Consola.pedirPrecio()
        modificada = controlador.servicio.modificarPrecioPlanta(nombre, precio)
        if modificada:
            print(f"Precio modificado: {modificada.getDescripcion()} - Nuevo precio: {modificada.precio} €")
        else:
            print("No se encontró la planta")

    @staticmethod
    def buscarPlanta(controlador):
        nombre = Consola.pedirNombre()
        p = controlador.servicio.buscarPlanta(nombre)
        if p:
            print(f"Encontrada: {p.getDescripcion()}")
        else:
            print("No encontrada")

    @staticmethod
    def listarPlantas(controlador):
        plantas = controlador.servicio.listarPlantas()
        for p in plantas:
            print(f"{p.getDescripcion()} - Altura: {p.altura} cm - Precio: {p.precio} €")

    @staticmethod
    def buscarPorAltura(controlador):
        print("Altura mínima: ")
        min_alt = int(Escaner.pedirDato())
        print("Altura máxima: ")
        max_alt = int(Escaner.pedirDato())
        plantas = controlador.servicio.buscarPorAlturaEntre(min_alt, max_alt)
        for p in plantas:
            print(p.getDescripcion())

    @staticmethod
    def buscarPorPrecio(controlador):
        print("Precio máximo: ")
        precio = float(Escaner.pedirDato())
        plantas = controlador.servicio.buscarPorPrecioMenorA(precio)
        for p in plantas:
            print(p.getDescripcion())

        
    

