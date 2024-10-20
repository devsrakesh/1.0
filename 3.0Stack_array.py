class Stack:
    def __init__(self):
        self.stack = []  # Initialize an empty list to represent the stack

    def push(self, value):
        self.stack.append(value)  # Add element to the top of the stack

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()  # Remove and return the top element
        return "Stack is empty!"  # Return a message if the stack is empty

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]  # Return the top element without removing it
        return "Stack is empty!"  # Return a message if the stack is empty

    def is_empty(self):
        return len(self.stack) == 0  # Check if the stack is empty

    def size(self):
        return len(self.stack)  # Return the number of elements in the stack

    def display(self):
        print("Stack:", self.stack)

# Example usage:
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
print(f"Popped element: {stack.pop()}")
stack.display()
print(f"Top element: {stack.peek()}")
print(f"Is stack empty?: {stack.is_empty()}")
print(f"Stack size: {stack.size()}")
