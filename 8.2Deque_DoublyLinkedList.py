class DNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedListDeque:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add_first(self, item):
        new_node = DNode(item, None, self.head)
        if self.is_empty():
            self.tail = new_node
        else:
            self.head.prev = new_node
        self.head = new_node

    def add_last(self, item):
        new_node = DNode(item, self.tail, None)
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
        else:
            self.head.prev = None
        return value

    def remove_last(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        value = self.tail.value
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
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
deque = DoublyLinkedListDeque()
deque.add_first(10)
deque.add_last(20)
print(deque)  # [10, 20]
deque.remove_first()
print(deque)  # [20]
deque.remove_last()
print(deque)  # []
