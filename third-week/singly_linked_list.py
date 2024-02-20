class Node:
    def __init__(self) -> None:
        self.element = None
        self.next = None

    def get_element(self):
        return self.element

    def set_element(self, value):
        self.element = value

    def get_next(self):
        return self.next

    def set_next(self, ref):
        self.next = ref

    def __str__(self) -> str:
        return str(self.get_element())

class SimplyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None and self.tail is None

    def insert_front(self, value):
        new_node = Node()
        new_node.set_element(value)
        new_node.set_next(self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        print(f"Inserted at front: {value}")

    def insert_back(self, value):
        new_node = Node()
        new_node.set_element(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
        print(f"Inserted at back: {value}")

    def insert_after(self, existing_element, new_element):
        current = self.head
        while current:
            if current.get_element() == existing_element:
                new_node = Node()
                new_node.set_element(new_element)
                new_node.set_next(current.get_next())
                current.set_next(new_node)
                
                if current == self.tail:
                    self.tail = new_node
                
                print(f"Inserted {new_element} after {existing_element}")
                return
            current = current.get_next()
        print(f"Element {existing_element} not found.")

    def remove_front(self):
        if self.is_empty():
            print("Nothing to remove")
            return None
        value = self.head.get_element()
        if self.head == self.tail:  # If there's only one item
            self.tail = None
        self.head = self.head.get_next()
        return value

    def display(self):
        iterator = self.head
        print("List contents:", end=" ")
        while iterator:
            print(iterator.get_element(), end=" -> ")
            iterator = iterator.get_next()
        print("None")

class Queue(SimplyLinkedList):
    def __init__(self) -> None:
        super().__init__()

    def enqueue(self, value):
        self.insert_back(value)
        print(f"Enqueued: {value}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        value = super().remove_front()  # Explicitly use super() to call the method from the parent class
        print(f"Dequeued: {value}")
        return value

# Initial setup for SimplyLinkedList operations
print("Starting with SimplyLinkedList operations:")
simple_list = SimplyLinkedList()
simple_list.insert_front("Athens")
simple_list.insert_front("Paris")
simple_list.insert_front("Madrid")
simple_list.insert_back("Tirana")
simple_list.insert_front("Prague")
simple_list.insert_front("Rome")
simple_list.insert_after("Prague", "London")
simple_list.display()  # Display the list after all insertions

# Setup and operations for Queue
print("\nStarting with Queue operations:")
queue = Queue()

# Enqueue operations
print("Enqueue operations:")
queue.enqueue("Texas")  # Enqueue Texas
queue.display()         # Display the queue after enqueuing Texas

queue.enqueue("Sofia")  # Enqueue Sofia
queue.display()         # Display the queue after enqueuing Sofia

queue.enqueue("Brno")   # Enqueue Brno
queue.display()         # Display the queue after enqueuing Brno

# Dequeue operation
print("Dequeue operation:")
queue.dequeue()         # Dequeue the first element (Texas)
queue.display()         # Display the queue after dequeuing
