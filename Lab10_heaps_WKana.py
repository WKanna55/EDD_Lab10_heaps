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

    def copy_heap(self, heapobject):
        self.items = []
        self.size = 0
        for n in heapobject.items:
            self.insert(n)
        return self
    def k_bigger_element(self, k): #
        if k > self.size:
            raise Exception("elemento fuera de la lista")
        heapAux = MaxHeap().copy_heap(self)
        dato = None
        for n in range(k):
            dato = heapAux.remove()
        return dato

    @staticmethod
    def is_maxheap(array):
        index = 0
        while index < len(array):
            parent_index = (index - 1) // 2
            l_c_index = (index * 2) + 1
            r_c_index = (index*2)+2
            if parent_index >= 0:
                if array[index] > array[parent_index]:
                    return False
            if r_c_index < len(array):
                if array[index] < array[r_c_index]:
                    return False
            if l_c_index < len(array):
                if array[index] < array[l_c_index]:
                    return False
            index += 1
        return True
            #array1 = [10, 5, 2, 20]
            #array2 = [20, 10, 5, 3]

    @staticmethod
    def heapify(array):
        heap = MaxHeap()
        for n in array:
            heap.insert(n)
        return heap.items


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
#print(heap.items)
heap.insert(40)
#print(heap.items)
heap.insert(7)
heap.insert(3)
#print(heap.items)

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

    def insert(self, priority, value):
        element = Element_Queue(priority, value)
        super().insert(element)

    def bubble_up(self):
        index = self.size - 1
        while index > 0 and self.items[index].priority > self.items[self.parent(index)].priority:
            self.swap(index, self.parent(index))
            index = self.parent(index)


    def is_valid_parent(self, index):
        if not self.has_left_child(index):
            return True
        is_valid = self.items[index].priority >= self.left_child(index).priority
        if self.has_right_child(index):
            is_valid = is_valid and self.items[index].priority >= self.right_child(index).priority
        return is_valid

    def larger_child_index(self, index):
        if not self.has_left_child(index):
            return index
        if not self.has_right_child(index):
            return self.left_child_index(index)

        left = self.left_child(index).priority
        right = self.right_child(index).priority
        if left >= right:
            return self.left_child_index(index)
        else:
            return self.right_child_index(index)


cola = Priority_Queue()
cola.insert(5, "roberto")
cola.insert(2, "juan")
cola.insert(3, "maria")
cola.insert(10, "luisa")
#cola.print_heap()
cola.remove()
#print()
#cola.print_heap()

"""Ejercicio 04: Implementacion de una cola de prioridad con heap maximo (fin)"""

"""Ejercicio 05: Heapify (inicio)"""

array_desordenado = [5,10,8,20,16,12,22]
#print(array_desordenado)
array_ordenado = MaxHeap.heapify(array_desordenado)
#print(array_ordenado)

"""Ejercicio 05: Heapify (fin)"""

"""Ejercicio 06: Encontrar el Elemento k-esimo mas pequeño o grande (inicio)"""
#print(heap.k_bigger_element(3))
"""Ejercicio 06: Encontrar el Elemento k-esimo mas pequeño o grande (fin)"""

"""Ejercicio 07: maxheap verificador (inicio)"""
array1 = [10,5,2,20]
array2 = [20,10,5,3]
#print(MaxHeap.is_maxheap(array1))
#print(MaxHeap.is_maxheap(array2))
#print(heap.is_maxheap(heap.items))
"""Ejercicio 07: maxheap verificador (fin)"""

"""Ejercicio 08: minheap con nodos (inicio)"""
class Nodo:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(f"Clave: {self.key} - valor: {self.value}")

class MinHeap:
    def __init__(self) -> None:
        self.items = []
        self.size = 0

    def insert(self, key, value):
        nodo = Nodo(key, value)
        self.items.append(nodo)
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
        while index > 0 and self.items[index].key < self.items[self.parent(index)].key:
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def bubble_down(self):
        index = 0
        while index <= self.size and not self.is_valid_parent(index):
            smaller_child_index = self.smaller_child_index(index)
            self.swap(index, smaller_child_index)
            index = smaller_child_index

    # Return if the index is a valid parent
    def is_valid_parent(self, index):
        if not self.has_left_child(index):
            return True
        is_valid = self.items[index].key >= self.left_child(index).key
        if self.has_right_child(index):
            is_valid = is_valid and self.items[index].key <= self.right_child(index).key
        return is_valid

    def swap(self, first, second):
        temp = self.items[first]
        self.items[first] = self.items[second]
        self.items[second] = temp

    def parent(self, index):  # Get index parent
        return (index - 1) // 2

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
    def smaller_child_index(self, index):
        if not self.has_left_child(index):
            return index
        if not self.has_right_child(index):
            return self.left_child_index(index)

        left = self.left_child(index).key
        right = self.right_child(index).key
        if left <= right:
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


heapmin = MinHeap()
heapmin.insert(5, "azucar")
heapmin.insert(6, "leche")
heapmin.insert(3, "arroz")
heapmin.insert(1, "pollo")
#heapmin.print_heap()

"""Ejercicio 08: minheap con nodos (fin)"""

"""Ejercicio 09: Min priority queue (inicio)"""

class MinPriorityQueue(MinHeap):
    def add(self, priority: int, value: str):
        super().insert(priority, value)
    def isempty(self):
        return self.size == 0

    def print_queue(self):
        super().print_heap()

minqueue = MinPriorityQueue()
minqueue.add(5, "Funel")
minqueue.add(6, "Liz")
minqueue.add(4, "Renato")
minqueue.add(2, "Luz")
minqueue.add(8, "Edward")
minqueue.add(1, "Eowyn")
#minqueue.print_queue()
minqueue.remove()
minqueue.remove()
minqueue.remove()
#print()
#minqueue.print_queue()
minqueue.remove()
minqueue.remove()
minqueue.remove()
#print(minqueue.isempty())

"""Ejercicio 09: Min priority queue (fin)"""

