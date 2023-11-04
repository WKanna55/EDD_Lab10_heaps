"""Implementacion de heaps (inicio)"""


class Heap:  # Max Heap
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


"""Implementacion de heaps (fin)"""

"""Implementacion heapsort(inicio)"""


# complejidad de tiempo O(n(log(n)))

class HeapSort(Heap):
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
heap = Heap()
heap.insert(30)
heap.insert(20)
heap.insert(10)
heap.insert(5)
print(heap.items)
heap.insert(40)
print(heap.items)
heap.remove()
print(heap.items)

ordenamiento = HeapSort()

print("\n\n")

array = [6,4,8,12,25,14,3,19]
print(array)
array_ordenado = ordenamiento.ordenar(array)

print(array_ordenado)
