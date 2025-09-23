# Instrucciones

Crea una clase abstracta `Planta` con los atributos:
- nombre (String)
- altura (int, en cm)
- precio (double)

Implementa validaciones básicas en métodos separados:
- La altura debe estar entre 5 cm y 300 cm.
- El precio debe ser positivo.

Crea una excepción base `PlantaException` que herede de `Exception`.

Implementa dos subclases:
- **Cactus** con atributo: tieneEspinas (boolean)
- **Flor** con atributo: color (String)

Declara un método abstracto `getDescripcion()` en `Planta`, e impleméntalo en cada subclase para mostrar información específica.

Crea una interfaz `ViveroInterface` con los métodos indicados más adelante.

Implementa una clase `ViveroVillanueva` que implemente la interfaz y utilice una colección interna para almacenar las plantas.

En el método `main`, que se te facilita, debes completar el código.

## Ejecución y salida

La ejecución del programa debe reflejar claramente las validaciones y la descripción de cada planta:

- Planta añadida: Cactus con espinas
- Planta añadida: Flor roja
- Error: El precio debe ser mayor que 0
- Error: La altura debe estar entre 5 y 300 cm
- Flor roja - Altura: 40 cm - Precio: 7.5 €
- Cactus sin espinas - Altura: 25 cm - Precio: 5.0 €

## Código base

### Clases y métodos principales

#### Planta (abstracta)

```java
public Planta(String nombre, int altura, double precio) throws PlantaException
public String getNombre()
public void setNombre(String nombre)
public int getAltura()
public void setAltura(int altura) throws PlantaException
public double getPrecio()
public void setPrecio(double precio) throws PlantaException
public abstract String getDescripcion()
```

#### Cactus (extends Planta)

```java
public Cactus(String nombre, int altura, double precio, boolean tieneEspinas) throws PlantaException
public boolean isTieneEspinas()
public void setTieneEspinas(boolean tieneEspinas)
@Override public String getDescripcion()
```

#### Flor (extends Planta)

```java
public Flor(String nombre, int altura, double precio, String color) throws PlantaException
public String getColor()
public void setColor(String color)
@Override public String getDescripcion()
```

#### PlantaException (extends Exception)

```java
public PlantaException(String mensaje)
```

### Código fuente de la interfaz ViveroInterface

```java
import java.util.List;

public interface ViveroInterface {
    void agregarCactus(String nombre, int altura, double precio, boolean tieneEspinas) throws PlantaException;
    void agregarFlor(String nombre, int altura, double precio, String color) throws PlantaException;
    Planta buscarPlanta(String nombre);  // Devuelve una planta o null si no la encuentra
    Planta modificarPrecioPlanta(String nombre, double precio);  // Cambia el precio a la primera planta que tengan ese nombre. Devuelve la planta modificada o null si no la encuentra
    Planta eliminarPrimeraPlantaConNombre(String nombre) throws PlantaException;  // Lanza excepción en caso de no encontrar ninguna planta con este nombre. Devuelve la planta retirada de la colección
    List<Planta> listarPlantas();  // Devuelve una copia de la lista de plantas
    List<Planta> buscarPorAlturaEntre(int alturaMin, int alturaMax); // Devuelve una lista de plantas cuya altura se encuentre entre el valor mínimo y el máximo incluidos
    List<Planta> buscarPorPrecioMenorA(double precio); // Devuelve una lista de plantas cuyo precio sea inferior o igual al recibido
}
```

### Código fuente de la clase Main

Debes rellenar los huecos:

```java
import java.util.List;

public class Main {
    public static void main(String[] args) {
        ViveroInterface vivero = new ViveroVillanueva();

        ____________ {
            vivero.agregarCactus("Cactus del desierto", 30, 5.0, true);
            System.out.println("Planta añadida: Cactus del desierto");

            vivero.agregarFlor("Rosa", 40, 7.5, "roja");
            System.out.println("Planta añadida: Rosa");

            vivero.agregarFlor("Tulipán", 50, 0, "amarillo");
            vivero.agregarCactus("Mini cactus", 2, 4.0, false);
        } _______________________________________________ {
            ________________________________________________________________________________
        }

        System.out.println("\nListado de plantas registradas:");
        for (Planta p : vivero.listarPlantas()) {
            System.out.println(p.getDescripcion() + " - Altura: " + p.getAltura() + " cm - Precio: " + p.getPrecio() + " €");
        }

        System.out.println("\nPlantas con altura entre 30 y 50 cm:");
        List<Planta> medias = vivero.buscarPorAlturaEntre(30, 50);
        for (Planta p : medias) {
            System.out.println(p.getDescripcion());
        }

        System.out.println("\nPlantas con precio menor o igual a 6 €:");
        List<Planta> baratas = vivero.buscarPorPrecioMenorA(6.0);
        for (Planta p : baratas) {
            System.out.println(p.getDescripcion());
        }

        ____________ {
            Planta eliminada = vivero.eliminarPrimeraPlantaConNombre("Rosa");
            System.out.println("\nPlanta eliminada: " + eliminada.getDescripcion());
        } _______________________________________________ {
            ________________________________________________________________________________
        }

        Planta buscada = vivero.buscarPlanta("Tulipán");
        System.out.println("\nResultado de búsqueda de Tulipán: " +
            (buscada != null ? buscada.getDescripcion() : "No encontrada"));

        Planta modificada = vivero.modificarPrecioPlanta("Cactus del desierto", 6.5);
        if (modificada != null) {
            System.out.println("\nPrecio modificado: " + modificada.getDescripcion() +
                " - Nuevo precio: " + modificada.getPrecio() + " €");
        } else {
            System.out.println("\nNo se encontró la planta para modificar el precio.");
        }
    }
}
```
