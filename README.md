1. Nombre completo del autor(a): Isaac Joel Rivero Peñarrieta

2. Breve descripción del proyecto

-Este proyecto está dedicado a la creación de un simulador y solucionador del Cubo Rubik en Python. Mediante la programación, he diseñado un
 sistema que permite cargar configuraciones del cubo desde un archivo, realizar movimientos y buscar soluciones mediante diferentes 
 algoritmos. Es una herramienta útil para entender mejor el funcionamiento del Cubo Rubik y experimentar con algoritmos de búsqueda y
  resolución.

3. Requerimientos del entorno de programación
-Se necesita Python 3.8 o superior.
-Librerías: 
    'tkinter' para la interfaz gráfica en python.
    'copy' para realizar copias profundas de los objetos del cubo.
    'collections.deque' para utilizar colas en la implementación del algoritmo BFS.

4. Manual de uso
    4.1 Formato de codificación para cargar el estado de un cubo desde el archivo de texto
        -El archivo debe contener 18 líneas, cada línea representa una fila del cubo, organizadas por caras en un orden específico (por 
        ejemplo, blanco, verde, naranja, etc.). Cada línea debe tener exactamente tres caracteres que representan el color de cada cuadro en 
        la fila.
        Cara 'U' (Superior) - Blanco (W)
        W W W
        W W W
        W W W

        Cara 'F' (Frontal) - Verde (G)
        G G G
        G G G
        G G G

        Cara 'L' (Izquierda) - Naranja (O)
        O O O
        O O O
        O O O

        Cara 'R' (Derecha) - Rojo (R)
        R R R
        R R R
        R R R

        Cara 'B' (Trasera) - Azul (B)
        B B B
        B B B
        B B B

        Cara 'D' (Inferior) - Amarillo (Y)
        Y Y Y
        Y Y Y
        Y Y Y

    4.2 Instrucciones para ejecutar el programa
    Para ejecutar el simulador:
        1.  Abre la terminal o consola.
        2.  Navega hasta el directorio donde se encuentran los archivos del proyecto. Asegúrate de que los archivos rubik_cube.py,
            rubik_moves.py, rubik_cube_GUI, rubik_a_star.py y rubik_ida_star.py estén en el mismo directorio.

        3. Ejecuta python rubik_cube_GUI.py para iniciar la interfaz gráfica.
                Ejemplo:
                'cd ruta/del/proyecto'
                PS C:\Users\8.1\Desktop\RUBIK> cd CUBO
                PS C:\Users\8.1\Desktop\RUBIK\CUBO> python rubik_cube_GUI.py

                NOTA: La solucion para el archivo cargado configuracion_cubo3.txt de acuerdo al simulador es: 

                L B L F U U D_prime R R B_prime L F R D R R F F D_prime F F U_prime R R L L U U

                (Esta solucion si las copias y colocas en el textbox comprueba que los movimientos sean correctos y muevan hasta resolver.)

        4. Utiliza los botones en la interfaz para realizar movimientos, resolver o reiniciar el cubo.
            Una vez que la interfaz gráfica esté abierta, podrás utilizar los botones proporcionados para interactuar con el cubo:
            Realizar Movimientos: Utiliza los botones en la interfaz para girar las caras del cubo en diferentes direcciones.
            Resolver el Cubo: Si deseas resolver el cubo automáticamente, busca y selecciona el botón de "resolver" o una opción similar.
            Reiniciar el Cubo: En caso de que desees comenzar de nuevo con un cubo en su estado inicial, busca y selecciona el botón de "reiniciar" o similar.


5. Diseño e implementación
    5.1. Breve descripción de modelo del problema
    -El modelo del problema se basa en la representación del estado del Cubo de Rubik como un grafo dirigido, donde cada nodo representa un 
    estado del cubo y las aristas representan los movimientos válidos entre estados. Se implementa en Python utilizando una estructura de 
    datos que permite manipulaciones eficientes y almacenamiento compacto de los estados del cubo. Cada estado del cubo se representa 
    mediante una combinación de las posiciones y orientaciones de las piezas, lo que permite realizar operaciones como rotaciones y 
    permutaciones de manera precisa y eficiente

    5.2. Explicación y justificación de algoritmo(s), técnicas, heurísticas seleccionadas
    -Breadth-First Search (BFS):
        El algoritmo BFS es una estrategia de búsqueda ciega que explora todos los nodos vecinos de un nodo actual antes de pasar a los 
        siguientes niveles de profundidad. Es útil cuando el costo de cada movimiento es uniforme y no se necesita considerar ninguna heurística.
        En mi caso, para implementar BFS, creamos una cola (queue) de nodos que representan estados del cubo. Comenzamos desde el estado 
        inicial y aplicamos todas las posibles combinaciones de movimientos de Rubik a cada estado para encontrar la solución. Este proceso 
        continúa hasta que encontramos el estado objetivo o agotamos todas las posibilidades.
    
    -A* Search:
        A* es un algoritmo de búsqueda informada que utiliza una combinación de costos reales y estimados (heurística) para determinar la
        mejor ruta a seguir. La heurística guía la búsqueda hacia la solución, priorizando los nodos que parecen estar más cerca del
        objetivo.
        En la implementación de A*, cada estado del cubo tiene asociado un costo que es la suma de la longitud del camino desde el estado 
        inicial más una estimación de la distancia al objetivo (heurística). Utilizamos una heurística simple que cuenta el número de piezas 
        fuera de lugar en cada cara del cubo.
    
    -Iterative Deepening A* (IDA*)
        IDA* es una variante de A* que resuelve el problema de la memoria limitada de A* al usar una búsqueda en profundidad limitada.
        Realiza iteraciones sucesivas, aumentando el límite de profundidad en cada iteración hasta que encuentra la solución.
        Mi implementación de IDA* comienza con una estimación inicial basada en la heurística. Luego, realiza búsquedas en profundidad 
        limitadas, ajustando el límite de profundidad según sea necesario hasta que encuentra la solución.
        Esta manera de estimar es bastante sencilla porque solo necesito mirar cada pieza y verificar si está en su lugar o no, en lugar de 
        complicarme con cálculos más difíciles que consideren la posición exacta de cada pieza respecto a las demás. Esto hace que mi 
        búsqueda de la solución sea más directa y me orienta sobre cuál movimiento podría acercarme más a la solución final.

    - Justificación de las técnicas y heurísticas seleccionadas
        BFS: Optamos por BFS debido a su simplicidad y garantía de encontrar la solución más corta en términos de movimientos. Dado que el 
        Cubo Rubik tiene un espacio de estados relativamente pequeño, BFS es viable y eficaz en este contexto. 

        A*: Elegimos A* debido a su capacidad para encontrar soluciones de manera más eficiente que BFS, gracias a la heurística que guía la 
        búsqueda. La heurística que utilizamos, aunque simple, proporciona una estimación razonable de la distancia al objetivo y mejora 
        significativamente el rendimiento de la búsqueda.
        
        IDA*: IDA* es una opción excelente cuando la memoria es limitada y no se puede almacenar todo el espacio de búsqueda. Además, es 
        eficiente en términos de espacio y puede encontrar soluciones óptimas. La heurística que utilizamos es adecuada para IDA* ya que es 
        rápida de calcular y proporciona una guía útil para la búsqueda en profundidad limitada.


    5.3. En caso de usar modelos lingüísticos, incluir los prompts clave
    No se utilizé modelos lingüísticos.

6. Trabajo Futuro
    6.1. Lista de tareas inconclusas y/o ideas para continuar con el proyecto
    -Optimización de Algoritmos: Mejorar la eficiencia de los algoritmos existentes.
    -Interfaz Gráfica: Añadir más funcionalidades interactivas y mejorar la visualización del cubo.
    -Personalización: Permitir a los usuarios definir configuraciones personalizadas más fácilmente.
    -Expansión del Proyecto: Integrar el proyecto con hardware real para controlar un Cubo Rubik físico mediante comandos del software, 
    mediante el uso de IDE como Arduino.
    