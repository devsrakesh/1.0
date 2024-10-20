# Stack ADT implemented using singly linked list
class Node:
    def __init__(self, data):
        self.data = data  # Element of the node
        self.next = None  # Pointer to the next node

class Stack:
    def __init__(self):
        self.top = None  # Points to the top of the stack

    # Check if the stack is empty
    def is_empty(self):
        return self.top is None

    # Push an element to the stack
    def push(self, value):
        new_node = Node(value)  # Create a new node
        new_node.next = self.top  # Set the new node's next to current top
        self.top = new_node  # Update top to the new node
        print(f"Pushed {value} to the stack.")

    # Pop an element from the stack
    def pop(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        popped_node = self.top  # Get the top node
        self.top = self.top.next  # Move the top pointer to the next node
        print(f"Popped {popped_node.data} from the stack.")
        return popped_node.data

    # Peek at the top element of the stack
    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.top.data

    # Display the elements of the stack
    def display(self):
        if self.is_empty():
            print("Stack is empty!")
            return
        current = self.top
        print("Stack elements:")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    stack.pop()
    stack.display()
    print(f"Top element is: {stack.peek()}")
