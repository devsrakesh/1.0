class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size  # Initialize the array with None
        self.front = -1  # Initially, the front is -1 (empty state)
        self.rear = -1   # Initially, the rear is -1 (empty state)

    # Check if the queue is full
    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    # Check if the queue is empty
    def is_empty(self):
        return self.front == -1

    # Enqueue operation
    def enqueue(self, value):
        if self.is_full():
            print("Queue is full!")
            return
        # If queue is empty, set front to 0
        if self.front == -1:
            self.front = 0
        # Increment rear and wrap around using modulo operator
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        print(f"Enqueued {value}")

    # Dequeue operation
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        # Get the front element
        value = self.queue[self.front]
        # If there is only one element left, reset queue to empty state
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            # Increment front and wrap around using modulo operator
            self.front = (self.front + 1) % self.size
        print(f"Dequeued {value}")
        return value

    # Display the queue
    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        print("Queue elements are:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

# Example usage:
if __name__ == "__main__":
    size = int(input("Enter the size of the circular queue: "))
    cq = CircularQueue(size)
    
    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    cq.enqueue(40)
    
    cq.display()
    
    cq.dequeue()
    cq.display()
    
    cq.enqueue(50)
    cq.display()
    
    cq.enqueue(60)  # This will show the queue is full if the size is 4
