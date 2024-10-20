from collections import deque

# Function to check if a given string is a palindrome using a stack and a queue
def is_palindrome(s):
    # Remove spaces and convert the string to lowercase for case-insensitive comparison
    s = ''.join(s.split()).lower()

    # Initialize a stack (using a list) and a queue (using deque)
    stack = []
    queue = deque()

    # Add each character to both stack and queue
    for char in s:
        stack.append(char)
        queue.append(char)

    # Compare elements popped from stack and dequeued from queue
    while stack:
        # Pop from the stack (LIFO) and dequeue from the queue (FIFO)
        if stack.pop() != queue.popleft():
            return False  # If any character doesn't match, it's not a palindrome

    return True  # If all characters match, it's a palindrome

# Example usage
if __name__ == "__main__":
    string = input("Enter a string: ")
    if is_palindrome(string):
        print(f"'{string}' is a palindrome.")
    else:
        print(f"'{string}' is not a palindrome.")
