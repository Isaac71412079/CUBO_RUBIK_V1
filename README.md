1. Nombre completo del autor(a)
ISAAC JOEL RIVERO PEÑARRIETA

2. Breve descripción del proyecto
El proyecto RUBIK es una implementación del algoritmo A* para resolver el Cubo de Rubik de 3x3x3. El programa utiliza movimientos estándar del cubo y técnicas de búsqueda heurística para encontrar la solución más eficiente para reordenar el cubo a su estado original.

3. Requerimientos del entorno de programación
Necesitarás Python 3.8 o superior.
Se necesita la librería copy para la copia profunda de estructuras de datos.

4. Manual de uso
    4.1. Formato de codificación para cargar el estado de un cubo desde el archivo de texto
    El cubo se carga desde un archivo de texto donde cada línea representa una fila de una cara del cubo, con las caras en el siguiente orden: Frontal (F), Derecha (R), Posterior (B), Izquierda (L), Superior (U), e Inferior (D). Cada color se representa por su inicial en inglés (W - Blanco, G - Verde, O - Naranja, R - Rojo, B - Azul, Y - Amarillo).

    4.2. Instrucciones para ejecutar el programa
    Asegúrate de que los archivos rubik_cube.py, rubik_moves.py, y rubik_a_star.py estén en el mismo directorio.
    Guarda la configuración inicial del cubo en un archivo de texto (por ejemplo, configuracion_cubo.txt).
    Ejecuta el script rubik_a_star.py desde la línea de comandos:
    Copy code
    Ejemplo:
    PS C:\Users\8.1\Desktop\RUBIK\CUBO> python rubik_a_star.py

    El programa pedirá el nombre del archivo de configuración, ingresa el nombre del archivo y presiona Enter.
    El programa mostrará los movimientos necesarios para resolver el cubo. (NOTA: LA COMPILACIÓN CON ESTE ALGORITMO TARDA BASTANTE TIEMPO)

5. Diseño e implementación
    5.1. Breve descripción de modelo del problema
    El modelo del problema consiste en representar el estado del Cubo de Rubik como un objeto de Python que permite manipulaciones a través de movimientos definidos. Cada estado del cubo es un nodo en el espacio de búsqueda del algoritmo A*.

    5.2. Explicación y justificación de algoritmo(s), técnicas, heurísticas seleccionadas
    Se seleccionó el algoritmo A* debido a su eficiencia en la búsqueda de caminos mínimos en espacios de estados grandes y complejos como el del Cubo de Rubik. Para resolver el Cubo de Rubik, utilice una técnica que me ayuda a estimar cuán cerca estoy de solucionarlo. Imaginé que cada pieza del cubo tiene un lugar correcto donde debería estar cuando el cubo está completamente resuelto. Lo que hago es simplemente contar cuántas piezas no están en su lugar correcto. Esta cuenta me da una idea de cuánto trabajo me queda por hacer para resolver el cubo.

    Esta manera de estimar es bastante sencilla porque solo necesito mirar cada pieza y verificar si está en su lugar o no, en lugar de complicarme con cálculos más difíciles que consideren la posición exacta de cada pieza respecto a las demás. Esto hace que mi búsqueda de la solución sea más directa y me orienta sobre cuál movimiento podría acercarme más a la solución final.

    5.3. En caso de usar modelos lingüísticos, incluir los prompts clave
    No se utilizé modelos lingüísticos.

6. Trabajo Futuro
    6.1. Lista de tareas inconclusas y/o ideas para continuar con el proyecto
    Optimización de la Heurística: Talvez podría haber implementado heurísticas más avanzadas como la distancia de Manhattan para bloques o la base de datos de patrones para mejorar la eficiencia de la búsqueda pero debido al tiempo y otras tareas no me alcanzo a hacerlas.
    Interfaz Gráfica: Desarrollar una interfaz gráfica de usuario para facilitar la interacción con el programa y visualizar el proceso de resolución.
    Ampliación de Funcionalidades: Talvez permitir resolver otras variantes del cubo, como el 4x4x4 o 5x5x5.
    