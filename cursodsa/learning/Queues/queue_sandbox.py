from Node import Node

class Queue():
    def __init__(self, head_node = None, tail_node = None, size = 0, max_size = None):
        self.head_node = head_node
        self.tail_node = tail_node
        self.size = size
        self.max_size = max_size
        
    def peek(self):
        if(self.is_empty()):
            print("¡No hay nada que ver aquí!")
        else:
            return self.head_node.value

    def get_size(self): #Devolverá el valor de la propiedad size
        return self.size
        
    def has_space(self): #Devolverá True si la cola tiene espacio para otro nodo.
        if(self.max_size == None):
            return True
        elif(self.max_size > self.get_size()):
            return True
        else:
            return False
            
    def is_empty(self): #Devolverá True si el tamaño es 0.
        if(self.size == 0):
            return True

    def enqueue(self, value):
        if(self.has_space()):
            item_to_add = Node(value)
            print("¡Agregando " + str(item_to_add.get_value()) + " a la cola!")
            if(self.is_empty()):
                self.head_node = item_to_add
                self.tail_node = item_to_add
            else:
                item_to_add = self.next_node
                self.tail_node = item_to_add
            self.size += 1
        else:
            print("¡Lo sentimos, no hay más espacio!")