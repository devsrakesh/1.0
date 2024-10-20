class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value, index=None):
        new_node = Node(value)
        if index is None or self.head is None:
            # Insert at the end or into an empty list
            if self.head is None:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node
        else:
            # Insert at specific index
            if index == 0:
                new_node.next = self.head
                self.head = new_node
            else:
                current = self.head
                for i in range(index - 1):
                    if current is None:
                        raise IndexError("Index out of bounds")
                    current = current.next
                new_node.next = current.next
                current.next = new_node

    def delete(self, value):
        if self.head is None:
            return  # Empty list
        if self.head.value == value:
            self.head = self.head.next  # Remove head node
        else:
            current = self.head
            while current.next and current.next.value != value:
                current = current.next
            if current.next:  # If value is found
                current.next = current.next.next

    def search(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index  # Return index of the value
            current = current.next
            index += 1
        return -1  # Value not found

    def display(self):
        current = self.head
        linked_list = []
        while current:
            linked_list.append(current.value)
            current = current.next
        print("Linked List:", linked_list)

# Example usage:
linked_list = LinkedList()
linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(15, 1)  # Insert 15 at index 1
linked_list.display()
linked_list.delete(20)
linked_list.display()
print(f"Search 10: Found at index {linked_list.search(10)}")
