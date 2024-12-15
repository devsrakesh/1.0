class ArrayDeque:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def add_first(self, item):
        self.data.insert(0, item)

    def add_last(self, item):
        self.data.append(item)

    def remove_first(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.data.pop(0)

    def remove_last(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.data.pop()

    def first(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.data[0]

    def last(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.data[-1]

    def __str__(self):
        return str(self.data)


# Example usage:
deque = ArrayDeque()
deque.add_first(10)
deque.add_last(20)
print(deque)  # [10, 20]
deque.remove_first()
print(deque)  # [20]
deque.remove_last()
print(deque)  # []
