# Escribe debajo el codigo de la clase DoublyLinkedList y sus respectivos metodos     
# Recuerda importar la clase Node en este script
from Node_sandbox import Node 

class DoublyLinkedLis_Modified():
    ################## Clase DLL normal ########################
    def __init__(self, head_node = None, tail_node = None):
        self.head_node = head_node
        self.tail_node = tail_node

    def add_to_head(self, new_value):
        new_head = Node(new_value)
        current_head = self.head_node
        
        if (current_head is not None):
            current_head.set_prev_node(new_head)
            new_head.set_next_node(current_head)
            
        self.head_node = new_head
    
        if(self.tail_node is None):
            self.tail_node = self.head_node

    def add_to_tail(self, new_value):
        new_tail = Node(new_value)
        current_tail = self.tail_node
        
        if (current_tail is not None):
            current_tail.set_next_node(new_tail)
            new_tail.set_prev_node(current_tail)

        self.tail_node = new_tail
        
        if(self.head_node is None):
            self.head_node = self.tail_node

    def remove_head(self):
        removed_head = self.head_node
        if (removed_head is None):
            return None
    
        self.head_node = removed_head.get_next_node()
        
        if (removed_head == self.tail_node):
            self.remove_tail()
        
        return removed_head.get_value()
        
    def remove_tail(self):
        removed_tail = self.tail_node
        if (removed_tail is None):
            return None
    
        self.tail_node = removed_tail.get_prev_node()
        
        if (removed_tail == self.head_node):
            self.remove_head()
        
        return removed_tail.get_value()

    def remove_by_value(self, value_to_remove):
        node_to_remove = None
        current_node = self.head_node
        while (current_node is not None):
            if(current_node.get_value() == value_to_remove):
            #if(current_node == value_to_remove):
                node_to_remove = current_node
                break
            current_node = current_node.get_next_node()
        if (node_to_remove is None):
            return None
        
        if(node_to_remove == self.head_node):
            self.remove_head()
        elif(node_to_remove == self.tail_node):
            self.remove_tail()
        else:
            next_node = node_to_remove.get_next_node()
            prev_node = node_to_remove.get_prev_node()
            
            next_node.set_prev_node(prev_node)
            prev_node.set_next_node(next_node)

        return node_to_remove

    #encurntro un nodo que me coincida
    def find_node(self, value):
        current_node = self.head_node
        while current_node is not None:
            if current_node.value == value:
                return current_node
            else:
                current_node = current_node.next_node
        return None

    #Roto mis nodos
    def move_node(self, node, steps):
        current_node = node
        if steps > 0:
            for _ in range(steps):
                if current_node.next_node is not None:
                    current_node = current_node.next_node 
                else:
                    current_node = self.head_node     
        else:
            for _ in range(-steps):
                if current_node.prev_node is not None:
                    current_node = current_node.prev_node 
                else:
                    current_node = self.tail_node
        return current_node

    # Cifrar
    def caesar_cipher(self, strMessage, n):
        alph = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '
        ]
        alphabet_list = DoublyLinkedLis_Modified()
        for letter in alph:
            alphabet_list.add_to_tail(letter)
    
        ciphered_message = ""
    
        for c in strMessage:
            node_i = alphabet_list.find_node(c)
            new_node = alphabet_list.move_node(node_i, n)
            ciphered_message += new_node.value
        return ciphered_message

    # ataque de fuerza bruta
    def brute_force_attack(self, message, cardinality):
        alph = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '
        ]
        for i in range(cardinality):
            desC_message = self.caesar_cipher(message, i)
            print(desC_message)