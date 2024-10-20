class Queue:
    def __init__(self):
        self.queue = []  # Initialize an empty list to represent the queue

    def enqueue(self, value):
        self.queue.append(value)  # Add element to the end of the queue

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)  # Remove and return the front element
        return "Queue is empty!"  # Return a message if the queue is empty

    def front(self):
        if not self.is_empty():
            return self.queue[0]  # Return the front element without removing it
        return "Queue is empty!"  # Return a message if the queue is empty

    def is_empty(self):
        return len(self.queue) == 0  # Check if the queue is empty

    def size(self):
        return len(self.queue)  # Return the number of elements in the queue

    def display(self):
        print("Queue:", self.queue)

# Example usage:
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()
print(f"Dequeued element: {queue.dequeue()}")
queue.display()
print(f"Front element: {queue.front()}")
print(f"Is queue empty?: {queue.is_empty()}")
print(f"Queue size: {queue.size()}")
