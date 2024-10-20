
# Node class to represent each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Element of the node
        self.next = None  # Pointer to the next node


# Queue ADT implemented using singly linked list
class Queue:
    def __init__(self):
        self.front = None  # Points to the front of the queue
        self.rear = None   # Points to the rear of the queue

    # Check if the queue is empty
    def is_empty(self):
        return self.front is None

    # Enqueue an element to the queue
    def enqueue(self, value):
        new_node = Node(value)  # Create a new node
        if self.is_empty():
            self.front = self.rear = new_node  # Both front and rear point to the new node
        else:
            self.rear.next = new_node  # Link the new node at the end of the queue
            self.rear = new_node  # Move the rear pointer to the new node
        print(f"Enqueued {value} to the queue.")

    # Dequeue an element from the queue
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        dequeued_node = self.front  # Get the front node
        self.front = self.front.next  # Move the front pointer to the next node
        # If the front becomes None, set rear to None as well (queue becomes empty)
        if self.front is None:
            self.rear = None
        print(f"Dequeued {dequeued_node.data} from the queue.")
        return dequeued_node.data

    # Peek at the front element of the queue
    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.front.data

    # Display the elements of the queue
    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        current = self.front
        print("Queue elements:")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.display()
    queue.dequeue()
    queue.display()
    print(f"Front element is: {queue.peek()}")
