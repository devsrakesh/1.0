class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class SinglyLinkedListDeque:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add_first(self, item):
        new_node = Node(item, self.head)
        if self.is_empty():
            self.tail = new_node
        self.head = new_node

    def add_last(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def remove_first(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return value

    def remove_last(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        current = self.head
        if current.next is None:  # Single element
            value = current.value
            self.head = self.tail = None
            return value
        while current.next != self.tail:
            current = current.next
        value = self.tail.value
        self.tail = current
        self.tail.next = None
        return value

    def first(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.head.value

    def last(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.tail.value

    def __str__(self):
        result, current = [], self.head
        while current:
            result.append(current.value)
            current = current.next
        return str(result)


# Example usage:
deque = SinglyLinkedListDeque()
deque.add_first(10)
deque.add_last(20)
print(deque)  # [10, 20]
deque.remove_first()
print(deque)  # [20]
deque.remove_last()
print(deque)  # []
