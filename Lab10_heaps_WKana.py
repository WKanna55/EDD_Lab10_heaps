"""Ejercicio 01: Implementacion de un heap(maxheap) (inicio)"""
class MaxHeap:  # Max Heap
    def __init__(self) -> None:
        self.items = []
        self.size = 0

    def insert(self, value):
        self.items.append(value)
        self.size += 1
        self.bubble_up()

    def remove(self):
        root = self.items[0]
        self.items[0] = self.items[-1]
        del self.items[-1]
        self.size -= 1
        self.bubble_down()
        return root

    # Order property
    def bubble_up(self):
        index = self.size - 1
        while index > 0 and self.items[index] > self.items[self.parent(index)]:
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def bubble_down(self):
        index = 0
        while index <= self.size and not self.is_valid_parent(index):
            larger_child_index = self.larger_child_index(index)
            self.swap(index, larger_child_index)
            index = larger_child_index

    # Return if the index is a valid parent
    def is_valid_parent(self, index):
        if not self.has_left_child(index):
            return True
        is_valid = self.items[index] >= self.left_child(index)
        if self.has_right_child(index):
            is_valid = is_valid and self.items[index] >= self.right_child(index)
        return is_valid

    def swap(self, first, second):
        temp = self.items[first]
        self.items[first] = self.items[second]
        self.items[second] = temp

    def parent(self, index):  # Get index parent
        return (index - 1) // 2

    def parent_value(self, child_index):
        if child_index >= self.size:
            raise Exception("Indice invalido")
        parent_index = self.parent(child_index)
        return self.items[parent_index]

    def left_child(self, index):  # return left child value
        return self.items[self.left_child_index(index)]

    def right_child(self, index):  # return right child value
        return self.items[self.right_child_index(index)]

    def left_child_index(self, index):  # return left index
        return index * 2 + 1

    def right_child_index(self, index):  # return right index
        return index * 2 + 2

    def has_left_child(self, index):
        return self.left_child_index(index) < self.size

    def has_right_child(self, index):
        return self.right_child_index(index) < self.size

    # Return larger child between left and right
    def larger_child_index(self, index):
        if not self.has_left_child(index):
            return index
        if not self.has_right_child(index):
            return self.left_child_index(index)

        left = self.left_child(index)
        right = self.right_child(index)
        if left >= right:
            return self.left_child_index(index)
        else:
            return self.right_child_index(index)

    def print_heap(self):
        return self.print_heap_(0)
    def print_heap_(self, padre, nivel = 0):
        if padre < self.size:
            self.print_heap_(self.left_child_index(padre), nivel + 1)
            print((nivel * 4 * "-") + str(self.items[padre]))
            self.print_heap_(self.right_child_index(padre), nivel + 1)


"""Ejercicio 01: Implementacion de un heap(maxheap) (fin)"""
"""Implementacion heapsort(inicio)"""


# complejidad de tiempo O(n(log(n)))

class MaxHeapSort(MaxHeap):
    def __init__(self):
        super().__init__()

    def ordenar(self, array):
        array_ordenado = []
        for n in array:
            self.insert(n)

        for i in range(self.size):
            array_ordenado.append(self.remove())

        return array_ordenado


"""Implementacion heapsort(fin)"""

# Max Heap
heap = MaxHeap()
heap.insert(30)
heap.insert(20)
heap.insert(10)
heap.insert(5)
print(heap.items)
heap.insert(40)
print(heap.items)
heap.insert(7)
heap.insert(3)
print(heap.items)

"""Ejercicio 02: retornar padre (inicio)"""
#print(heap.parent_value(5))
"""Ejercicio 02: retornar padre (fin)"""

"""Ejercicio 03: imprimir heap (inicio)"""
#heap.print_heap()
"""Ejercicio 03: imprimir heap (fin)"""

"""Ejercicio 04: Implementacion de una cola de prioridad con heap maximo (inicio)"""
class Element_Queue:
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value
    def __str__(self):
        return str(f"Prioridad: {self.priority} valor: {self.value}")
class Priority_Queue(MaxHeap):
    def __init__(self):
        super().__init__()

    def insert(self, value):
        pass   

"""Ejercicio 04: Implementacion de una cola de prioridad con heap maximo (fin)"""

"""Ejercicio 05: Heapify (inicio)"""
"""Ejercicio 05: Heapify (fin)"""

"""Ejercicio 06: Encontrar el Elemento k-esimo mas pequeño o grande (inicio)"""
"""Ejercicio 06: Encontrar el Elemento k-esimo mas pequeño o grande (fin)"""

"""Ejercicio 07: maxheap (inicio)"""
"""Ejercicio 07: maxheap (fin)"""

"""Ejercicio 08: minheap con nodos (inicio)"""
"""Ejercicio 08: minheap con nodos (fin)"""

"""Ejercicio 09: Min priority queue (inicio)"""
"""Ejercicio 09: Min priority queue (fin)"""

