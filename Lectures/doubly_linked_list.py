class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:  # Deleting the head
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:  # Deleting the tail
                    self.tail = current.prev
                return
            current = current.next

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")
        
    def print_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
        
    def print_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")
        
    def insert_at_position(self, position, data):
        new_node = Node(data)
        if position < 0:
            raise IndexError("Position cannot be negative")

        if self.head is None:
            if position == 0:
                self.head = new_node
            else:
                raise IndexError("Position out of bounds")
            return
        
        if position == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return

        current = self.head
        current_position = 0

        while current.next and current_position < position - 1:
            current = current.next
            current_position += 1
        
        if current_position != position - 1 and current.next is None:
            raise IndexError("Position out of bounds")

        new_node.next = current.next
        new_node.prev = current

        if current.next:
            current.next.prev = new_node
        current.next = new_node
        
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None
    
    def replace(self, old_data, new_data):
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                return True
            current = current.next
        return False