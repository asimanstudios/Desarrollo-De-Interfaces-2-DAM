> # **<span style="color:green">Desarrollo de Interfaces</span>** 
---
> ## **Datos**
- **Autor:** Adrián Simarro Manzano
- **Github:** [Enlace de Perfil de Github](https://github.com/asimanstudios)
---
> ## **Breves apuntes de Markdown**
### Titualares
+ Se puede integrar codigo HTML normalmente en código MarkDown
# H1 ▶ # H1
## H2 ▶ ## H2
### H3 ▶ ### H3
### Listas
+ Las listas se pueden colocar con guiones en caso de ser desordenadas o con numeros usando tabulaciones. Se pueden usar (-,*,+) y otros caracteres especialel para las ordenadas. Las anidadas dependen de los interpretadores.

> **Desordenada**
- Item 1
    - Intem 2
    - Item3
- Item 4
> **Ordenada**
1. Item 1
    2. Intem 2
    3. Item3
2. Item 4
> **Mezclada**
1. Item 1
    - Intem 2
    - Item3
2. Item 4
#### Listas estilo TODO List
+ Markdown permite hacer listas a modo de todo list para marcarlas como realizadas en caso de estarlo. Metiendo una X en vez de un espacio marca como realizada la tarea o item en cuestión de la Todo List

- [x] Item 1
- [ ] Item 2
- [x] Item 3
- [ ] Item 4
### Emojis
+ Con los (: :) dentro podemos incluir emojis o meterlos desde windows + .
    - Ejemplo Computer -> :computer:
---
## Estilizados de texto
- Negrita: Doble asterisco en un texto cubriendolo **Hola Estoy en negrita**.
- Otra negrita: Cubrir con barras bajas __Hola estoy en negrita tambien__
- Cursiva: Una barra baja o un asterisco en vez de 2 *Cursiva*, _Cursiva_
- Tachado: Con doble birgulilla ~~Hola~~
- Subindce: 1 birgulilla ~Hola~ o con etiqueta <sub>Subindice</sub>
- Subperindice : Co etiqueta sup <sup>Subindice</sub>
- Subrayado: etiqueta ins <ins>Subrayado</ins>
- Citas o quotes : con el simbolo > podemos hacer citas
> Ejemplo quote
- Callout: > [info] texto . Esto no funciona ni en git ni visual pero si en obsidian y similares
> [Info] iNFO
> TEXTO
- Meter codigo: Se ponen ( `` ) Para poder meter codigo o textos preformateados.
` Esto es codigo  o texto preformateado simple`
```
Texto Preformateado, Párrafo

```
- Citas anidadas: mezclamos > para anidarlas:
> Esto es
> > Una Cita 
> > > Anidada
- Codificacion de diferentes lenguajes: tres comillas ``` y el nombre del lenjuaje. Los colores y demás dependeran del lenguaje y del renderizador.
> Esto es código Python: 
```python
print('hola mundo')

```
> Esto es código Java
```java
system.outn.println("Hola Mundo");

```
- Enlaces y vínculos:
    - Para esto usamos [Nombre del Link] (Url) (Sin espacio entre los corchetes y los parentesis si no no será funcional.)
    - Ejemplo: [Perfil](https://github.com/asimanstudios)

- Lincar titualares:
    - Para esto se pone entre parentesis la url y entre corchete el texto.
    - Ejemplo de enlace interno a la sección de estilizados de texto:
[Estilizados de Texto](#estilizados-de-texto)

    - Se pude aplicar esto a ficheros relativos dentro del repositorio para esto vamos a crear uno de ejemplo llamado leeme.txt.
    - Link: [Leeme txt](/leeme.txt)
---
## Imagenes
+ Se pueden incorporar imagenes dentro del texto medieante un enlace a la imagen. Poniendole una exclamacion antes del corchete.

![Nutrias](https://www.wnct.com/wp-content/uploads/sites/99/2022/08/All-Three-Best.jpg)
> Nutrias imagen de ejemplo.
+ Para el tamaño se pone esta barra | y el tamaño que le queremos poner aunque depende mucho del renderizador.

---
## PDF
+ En ciertos renderizadores podemos insertar documentos pdf dentro del documento a modo de enlace mas en los basicos no es de todo posible.
---
## Mencionar personas y equipos
+ Esto es muy propio de github mediante @ y el usuario en cuestion.
+ Ejemplo @asimanstudios 
- Depende del interprete el poderse ver.
---
## ALERTAS
+ Es posible renderizarlo en github y algun otro renderizador en siitos como visual studio no es posible.

> [!NOTE]
> TEXTO

> [!TIP]
> TEXTO

> [!IMPORTANT]
> TEXTO

> [!WARNING]
> TEXTO

> [!CAUTION]
> TEXTO
