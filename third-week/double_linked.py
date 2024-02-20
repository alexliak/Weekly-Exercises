class Node:
    def __init__(self, value=None):
        self.element = value  # Store the value of the node
        self.next = None  # Reference to the next node in the list
        self.prev = None  # Reference to the previous node in the list

    def get_element(self):
        return self.element

    def set_element(self, value):
        self.element = value

    def get_next(self):
        return self.next

    def set_next(self, ref):
        self.next = ref

    def get_prev(self):
        return self.prev

    def set_prev(self, ref):
        self.prev = ref

    def __str__(self):
        return str(self.get_element())
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Start of the list
        self.tail = None  # End of the list

    def is_empty(self):
        return self.head is None and self.tail is None  # Check if the list is empty

    def insert_front(self, value):
        # Create a new node
        new_node = Node(value)
        new_node.set_next(self.head)  # New node's next points to the current head
        if not self.is_empty():
            self.head.set_prev(new_node)  # Current head's prev points to new node
        else:
            self.tail = new_node  # If list was empty, new node is also the tail
        self.head = new_node  # Update the head to the new node
        print(f"Inserted '{value}' at the front.")

    def insert_back(self, value):
        # Create a new node
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node  # New node is the head if list was empty
        else:
            self.tail.set_next(new_node)  # Current tail's next points to new node
            new_node.set_prev(self.tail)  # New node's prev points to current tail
        self.tail = new_node  # Update the tail to the new node
        print(f"Inserted '{value}' at the back.")

    def display(self):
        current = self.head
        if self.is_empty():
            print("List is empty.")
            return
        print("List contents:", end=" ")
        while current:
            print(current.get_element(), end=" <-> " if current.get_next() else "")
            current = current.get_next()
        print("\n")

        # Creating a new DoublyLinkedList instance
dll = DoublyLinkedList()

# Inserting elements at the front and back
dll.insert_front("C")
dll.insert_front("B")
dll.insert_front("A")  # List after these insertions: A <-> B <-> C
dll.insert_back("D")
dll.insert_back("E")   # Final list: A <-> B <-> C <-> D <-> E

# Displaying the list contents
print("After all insertions:")
dll.display()

# The `insert_after`, `remove_front`, and `remove_back` methods would need to be implemented similarly,
# with proper management of both `next` and `prev` pointers to maintain the list's integrity.
