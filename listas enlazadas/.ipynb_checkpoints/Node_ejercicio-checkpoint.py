# Uso de la clase Node con tareas domesticas
from Node_sandbox import Node

# Creación de instancias  
tarea1 = Node("Comprar víveres", None)
tarea2 = Node("Estudiar para el examen", None)
tarea3 = Node("Hacer ejercicio", None)

# Acceder a los valores y establecer relaciones
tarea1.set_next_node(tarea2)
tarea2.set_next_node(tarea3)

# Imprimir los valores
print("Primer tarea:", tarea1.get_value())
print("Segunda tarea:", tarea1.get_next_node().get_value())
print("Tercer tarea:", tarea1.get_next_node().get_next_node().get_value())
