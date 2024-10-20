class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Stack:", self.stack)

# Helper function to define precedence of operators
def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0

# Function to check if a character is an operator
def is_operator(c):
    return c in ['+', '-', '*', '/', '^']

# Function to check if a character is an operand
def is_operand(c):
    return c.isalpha() or c.isdigit()

# Function to convert infix to postfix
def infix_to_postfix(expression):
    stack = Stack()  # Initialize stack
    postfix = []  # To store the postfix expression

    for char in expression:
        # If the character is an operand, add it to output
        if is_operand(char):
            postfix.append(char)
        # If the character is '(', push it to stack
        elif char == '(':
            stack.push(char)
        # If the character is ')', pop until '(' is encountered
        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
            stack.pop()  # Pop '(' from the stack
        # If the character is an operator
        elif is_operator(char):
            while (not stack.is_empty() and
                   precedence(char) <= precedence(stack.peek())):
                postfix.append(stack.pop())
            stack.push(char)

    # Pop all the remaining operators from the stack
    while not stack.is_empty():
        postfix.append(stack.pop())

    return ''.join(postfix)  # Convert list to string

# Example usage
if __name__ == "__main__":
    expression = input("Enter an infix expression: ")
    print("Postfix expression:", infix_to_postfix(expression))
