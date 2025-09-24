
from Vista.Consola import Escaner
from Servicio.ServiciosViviero import ServiciosVivero

class Consola():
    tipoPlanta = ""
    altura=0
    precio=0
    color=""
    espinas=False
    seleccion:0
    nombre=""

    def menuConsola():
        print("===========VIVIEROS VILLANUEVA===========")
        print("- Selecciona tu opción.")
        print("1. Agregar planta")
        print("2. Eliminar planta")
        print("3. Modificar planta")
        print("4. Salir")


    def mensajeSalida():
        print("Saliendo!")
    def mensajeError(mensaje:str):
        print ("Error: ", mensaje)
    
    def pedirTipo():
        print("Indica que tipo de planta es?: ")
        Escaner.pedirDato()
    def pedirNombre():
        print("Indica el nombre de la planta: ")
        Escaner.pedirDato()
    def pedirAltura():
        print("Indica la altura de tu planta: ")
        Escaner.pedirDato()
    def pedirPrecio():
        print("Indica el precio de tu planta: ")
        Escaner.pedirDato()
    def pedirColor():
        print("Indica el color de tu planta: ")
        Escaner.pedirDato()
    def pedirEspinas():
        print("Indica si tu planta tiene espinas:")
        Escaner.pedirDato()
    
    def ejecucionMenu():
        Consola.menu()
        seleccion=Escaner.pedirDato()
        if seleccion==1:
            tipo = Consola.pedirTipo()
            if (tipo.lower()=="planta"):
                  nombre= Consola.pedirNombre()
                  altura= Consola.pedirAltura()
                  precio= Consola.pedirPrecio()
            elif(tipo.lower()=="cactus"):
                nombre= Consola.pedirNombre()
                altura= Consola.pedirAltura()
                precio= Consola.pedirPrecio()
                espinas= Consola.pedirEspinas()
            elif(tipo.lower()=="flor"):
                nombre= Consola.pedirNombre()
                altura= Consola.pedirAltura()
                precio= Consola.pedirPrecio()
                color= Consola.pedirColor()
            else:    
                Consola.mensajeError("Error de tipo. Tipo de planta no existente.")                       
        elif seleccion==2:
            Escaner.pedirDato()
        elif seleccion==3:
            Escaner.pedirDato()
        else:
            Consola.mensajeError("Seleccion Invalida")

        
    

