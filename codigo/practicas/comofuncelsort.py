#Componentes Clave "de Timsort
#Identificación de Runs (Sublistas Ordenadas)

#Runs Ascendentes y Descendentes: Timsort comienza identificando sublistas ya ordenadas en la lista original. Estas sublistas pueden estar ordenadas de forma ascendente o descendente. Si una sublista está en orden descendente, Timsort la invierte para que todas las runs sean ascendentes.
#Tamaño Mínimo de Run (minrun): Para mejorar la eficiencia, Timsort asegura que cada run tenga al menos un tamaño mínimo (minrun). Si una run es más corta que minrun, Timsort utiliza Insertion Sort para extenderla hasta alcanzar este tamaño.
#Ordenación de Runs Pequeños

#Insertion Sort: Las runs pequeñas se ordenan utilizando Insertion Sort, que es eficiente para listas pequeñas o casi ordenadas. Este paso es rápido debido a la naturaleza adaptativa de Insertion Sort.
#Fusión de Runs (Merge)

#Merge Sort: Una vez que todas las runs tienen un tamaño adecuado, Timsort las fusiona de manera similar a Merge Sort. Este proceso de fusión es eficiente porque las runs ya están parcialmente ordenadas.
#Optimización de Galloping: Timsort implementa una técnica llamada "galloping" para acelerar la fusión cuando una de las dos runs a fusionar tiene muchos elementos consecutivos que ya están en orden.
#Mantenimiento de una Pila de Runs

#Timsort utiliza una pila para mantener un registro de las runs pendientes de fusión. Aplica ciertas reglas de invariantes para decidir cuándo fusionar las runs en la pila, lo que garantiza que el proceso de fusión sea eficiente y equilibrado.
#Paso a Paso del Funcionamiento de Timsort
#División en Runs:

#Comienza recorriendo la lista y detectando runs ascendentes o descendentes.
#Invierte las runs descendentes para convertirlas en ascendentes.
#Si una run es más corta que minrun, aplica Insertion Sort para extenderla.
#Fusión de Runs:

#Utiliza la pila de runs para fusionar runs adyacentes.
#Sigue las reglas de invariante de Timsort para mantener un balance adecuado en la pila.
#Aplica Merge Sort para fusionar las runs, optimizando con galloping cuando es posible.
#Finalización:

#Repite el proceso de fusión hasta que quede una única run que representa la lista completamente ordenada.
#Ventajas de Timsort
#Estabilidad: Mantiene el orden relativo de elementos iguales, lo cual es importante en muchas aplicaciones.
#Adaptabilidad: Aprovecha las runs ya ordenadas en la lista, lo que lo hace muy eficiente para listas parcialmente ordenadas.
#Eficiencia: Tiene una complejidad de tiempo de O(n log n) en el peor de los casos, pero puede ser más rápido en práctica debido a sus optimizaciones.