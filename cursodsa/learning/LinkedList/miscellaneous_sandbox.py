# miscellaneous_sandbox.py

from Node import Node
from LinkedList_sandbox import LinkedList

def nth_last_element(ll, n):
    main_ptr = ll.get_head_node()
    ref_ptr = ll.get_head_node()

    count = 0
    while count < n:
        if ref_ptr is None:
            print("La lista es más corta que n elementos.")
            return None
        ref_ptr = ref_ptr.get_next_node()
        count += 1

    while ref_ptr is not None:
        main_ptr = main_ptr.get_next_node()
        ref_ptr = ref_ptr.get_next_node()

    if main_ptr:
        return main_ptr.get_value()
    else:
        return None

