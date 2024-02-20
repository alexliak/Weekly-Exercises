class Node:
    # Constructor for the node
    def __init__(self, value):
        self.value= value # Value stored in the node
        self.next= None # Pointer to the next node

class LinkedList:
    # Constructor for the likned list
    def __init__(self):
        self.head= None # The head (start) of the list, initially None
         
    def insert_back(self, value):
        """Adds a node with the specific value to the end of the list"""
        new_node= Node(value)  # Create a new node with the provided value
        if not self.head: # If the list is empty make the new node the head
            self.head= new_node 
            print(f"Inserted {value} as the head")
            return
        # If the list is not empty, find the last node
        current=self.head
        while current.next: # Traverse untill the last node 
            current= current.next
        # After finding the last node, points its 'next' to the new node
        current.next= new_node
        print(f"Inserted {value} at the back")
        
    def remove(self, value):
        """Removes the first node that contains the specific value"""
        current= self.head
        if current and current.value == value: # If the node to remove is the head
            self.head= current.nextn#Move the head pointer to the next node
            print(f"Remove {value} from the list")
            return
        
        # If the node to remove is not the head, find the node
        prev= None # Keep track of the previous node
        while current and current.value != value: # Traverse the list
            prev = current
            current = current.next
        if current: # If the node is found
            prev.next = current.next #Remove the node be changing the next point
            print(f"Removed {value} from the list")
        else: # If the node with the value was not found
            print(f"Value {value} not found in the list")
            
    def print_list(self):
        """Prints all the values in the list"""
        current= self.head
        if not current: # If the list is empty
            print("The list is empty")
            return
        
        # If the list not empty, prints its contents
        print("LinkedList contents:", end=" ")
        while current: # Traverse the list
            print(current.value, end=" ->" if current.next else "")
            current = current.next
        print() # New line at the end of the list
        
class Queue(SinglyLinkedList):
    def __init__(self):
        super().__init__()

    def enqueue(self, value):
        """Add an element to the end of the queue."""
        self.insert_back(value)  # Utilizes the insert_back method from SinglyLinkedList
        print(f"Enqueued {value}")

    def dequeue(self):
        """Remove and return the front element of the queue."""
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        value = self.remove_first()  # Utilizes the remove_first method from SinglyLinkedList
        print(f"Dequeued {value}")
        return value



# Initialize the linked list
ll = LinkedList()

# Add nodes in the list
ll.insert_back(1)
ll.insert_back(2)
ll.insert_back(3)

ll.print_list()
ll.remove(2)
ll.print_list()