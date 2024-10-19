# Clase Node - Representa un nodo en la lista enlazada
class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

    def get_info(self):
        return self.info

    def set_next(self, next_node):
        self.next = next_node

    def get_next(self):
        return self.next


# Clase Order - Representa un pedido con cliente y cantidad
class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def print_info(self):
        print(f"     Customer: {self.customer}")
        print(f"     Quantity: {self.qtty}")
        print("     ------------")


# Clase Queue - Implementa la cola con una lista enlazada
class Queue:
    def __init__(self):
        self._front = None  # Primer nodo de la cola
        self._rear = None   # Último nodo de la cola
        self.size = 0       # Tamaño de la cola

    # Retorna el tamaño de la cola
    def get_size(self):
        return self.size

    # Verifica si la cola está vacía
    def is_empty(self):
        return self._front is None

    # Devuelve el primer elemento de la cola sin eliminarlo
    def front(self):
        if self.is_empty():
            return None
        return self._front.get_info()

    # Agrega un nuevo elemento al final de la cola
    def enqueue(self, info):
        new_node = Node(info)
        if self.is_empty():
            self._front = new_node
            self._rear = new_node
        else:
            self._rear.set_next(new_node)
            self._rear = new_node
        self.size += 1

    # Elimina y devuelve el primer elemento de la cola
    def dequeue(self):
        if self.is_empty():
            return None
        info = self._front.get_info()
        self._front = self._front.get_next()
        self.size -= 1
        if self.is_empty():
            self._rear = None
        return info

    # Imprime la información de todos los elementos de la cola
    def print_info(self):
        print("********* QUEUE DUMP *********")
        print(f"   Size: {self.size}")
        current = self._front
        position = 1
        while current is not None:
            print(f"   ** Element {position}")
            order = current.get_info()
            order.print_info()
            current = current.get_next()
            position += 1
        print("******************************")

    # Devuelve el n-ésimo elemento de la cola sin eliminarlo
    def get_nth(self, pos):
        if pos < 1 or pos > self.size:
            return None
        current = self._front
        index = 1
        while index < pos:
            current = current.get_next()
            index += 1
        return current.get_info()


# Clase TestQueue para probar la funcionalidad de la cola
def test_queue():
    # Crear una nueva cola
    queue = Queue()

    # Crear 4 pedidos
    order1 = Order(20, "cust1")
    order2 = Order(30, "cust2")
    order3 = Order(40, "cust3")
    order4 = Order(50, "cust4")

    # Agregar los pedidos a la cola
    queue.enqueue(order1)
    queue.print_info()  # Ver el estado de la cola después de agregar order1

    queue.enqueue(order2)
    queue.print_info()  # Ver el estado de la cola después de agregar order2

    queue.enqueue(order3)
    queue.print_info()  # Ver el estado de la cola después de agregar order3

    queue.enqueue(order4)
    queue.print_info()  # Ver el estado de la cola después de agregar order4

    # Probar el método front() para ver el primer elemento sin eliminarlo
    print("Front of queue:")
    front_order = queue.front()
    if front_order is not None:
        front_order.print_info()

    # Probar el método dequeue() para eliminar el primer elemento
    print("Dequeue first element:")
    queue.dequeue()
    queue.print_info()  # Ver el estado de la cola después de eliminar el primer elemento

    # Probar el método get_nth() para obtener el tercer elemento sin eliminarlo
    print("3rd element in the queue:")
    third_order = queue.get_nth(3)
    if third_order is not None:
        third_order.print_info()


# Llamar a la función de prueba
test_queue()
