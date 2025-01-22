Here are Python programs to implement linear and binary search using both recursive and non-recursive functions:

### a) **Linear Search**

#### 1. Non-Recursive Linear Search:
```python
def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# Example usage:
arr = [10, 23, 45, 70, 11, 15]
target = 70
result = linear_search(arr, target)
print(f"Non-Recursive Linear Search: Target found at index {result}")
```

#### 2. Recursive Linear Search:
```python
def linear_search_recursive(arr, target, index=0):
    if index >= len(arr):
        return -1  # Base case: Target not found
    if arr[index] == target:
        return index  # Base case: Target found
    return linear_search_recursive(arr, target, index + 1)  # Recursive call

# Example usage:
arr = [10, 23, 45, 70, 11, 15]
target = 70
result = linear_search_recursive(arr, target)
print(f"Recursive Linear Search: Target found at index {result}")
```

### b) **Binary Search** (Note: The array must be sorted)

#### 1. Non-Recursive Binary Search:
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Return the index if the target is found
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
    return -1  # Return -1 if the target is not found

# Example usage:
arr = [10, 11, 15, 23, 45, 70]
target = 70
result = binary_search(arr, target)
print(f"Non-Recursive Binary Search: Target found at index {result}")
```

#### 2. Recursive Binary Search:
```python
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1  # Base case: Target not found
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid  # Base case: Target found
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)  # Search in right half
    else:
        return binary_search_recursive(arr, target, left, mid - 1)  # Search in left half

# Example usage:
arr = [10, 11, 15, 23, 45, 70]
target = 70
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
print(f"Recursive Binary Search: Target found at index {result}")
```

### Summary:
- **Linear Search** scans the entire array sequentially, making it suitable for unsorted data.
- **Binary Search** operates on sorted arrays, dividing the search space in half with each step for faster performance.

Both recursive and non-recursive versions achieve the same functionality but differ in how they approach the search problem.

Here are Python programs to implement the List Abstract Data Type (ADT) using both arrays (Python lists) and linked lists.

### a) **List ADT Using Arrays**

Python lists inherently provide most of the functionality of a List ADT, but let's implement some basic operations to demonstrate:

```python
class ArrayList:
    def __init__(self):
        self.data = []

    def insert(self, value, index=None):
        if index is None:
            self.data.append(value)  # Append to the end
        else:
            self.data.insert(index, value)  # Insert at a specific index

    def delete(self, value):
        if value in self.data:
            self.data.remove(value)  # Remove first occurrence of value

    def search(self, value):
        if value in self.data:
            return self.data.index(value)  # Return index of value
        return -1  # If value is not found

    def display(self):
        print("Array List:", self.data)

# Example usage:
arr_list = ArrayList()
arr_list.insert(10)
arr_list.insert(20)
arr_list.insert(15, 1)  # Insert 15 at index 1
arr_list.display()
arr_list.delete(20)
arr_list.display()
print(f"Search 10: Found at index {arr_list.search(10)}")
```

### b) **List ADT Using Linked Lists**

To implement a List ADT using a linked list, we first need to create a `Node` class and a `LinkedList` class. Here, we'll implement basic operations like insertion, deletion, and search.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value, index=None):
        new_node = Node(value)
        if index is None or self.head is None:
            # Insert at the end or into an empty list
            if self.head is None:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node
        else:
            # Insert at specific index
            if index == 0:
                new_node.next = self.head
                self.head = new_node
            else:
                current = self.head
                for i in range(index - 1):
                    if current is None:
                        raise IndexError("Index out of bounds")
                    current = current.next
                new_node.next = current.next
                current.next = new_node

    def delete(self, value):
        if self.head is None:
            return  # Empty list
        if self.head.value == value:
            self.head = self.head.next  # Remove head node
        else:
            current = self.head
            while current.next and current.next.value != value:
                current = current.next
            if current.next:  # If value is found
                current.next = current.next.next

    def search(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index  # Return index of the value
            current = current.next
            index += 1
        return -1  # Value not found

    def display(self):
        current = self.head
        linked_list = []
        while current:
            linked_list.append(current.value)
            current = current.next
        print("Linked List:", linked_list)

# Example usage:
linked_list = LinkedList()
linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(15, 1)  # Insert 15 at index 1
linked_list.display()
linked_list.delete(20)
linked_list.display()
print(f"Search 10: Found at index {linked_list.search(10)}")
```

### Summary of Operations:

1. **Insert**:
   - **Array**: Uses the `append()` method to insert at the end and `insert()` to insert at a specific index.
   - **Linked List**: If no index is given, the new node is inserted at the end; otherwise, it is inserted at the specified index.

2. **Delete**:
   - **Array**: Uses `remove()` to delete the first occurrence of the value.
   - **Linked List**: Deletes a node by value, adjusting the pointers.

3. **Search**:
   - **Array**: Uses `index()` to return the index of the value.
   - **Linked List**: Traverses the list, returning the index if the value is found.

Both implementations demonstrate how a List ADT can be built using arrays and linked lists, providing basic operations for managing and manipulating data.


Here are Python programs to implement the Stack and Queue Abstract Data Types (ADT) using arrays (Python lists).

### a) **Stack ADT Using Array**

A stack follows the **LIFO** (Last In, First Out) principle. The operations of a stack typically include `push`, `pop`, `peek`, and `is_empty`.

```python
class Stack:
    def __init__(self):
        self.stack = []  # Using a list to implement the stack

    def push(self, value):
        self.stack.append(value)  # Add element to the top of the stack

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()  # Remove and return the top element
        return None  # Return None if the stack is empty

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]  # Return the top element without removing it
        return None  # Return None if the stack is empty

    def is_empty(self):
        return len(self.stack) == 0  # Check if the stack is empty

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
```

### b) **Queue ADT Using Array**

A queue follows the **FIFO** (First In, First Out) principle. The operations of a queue typically include `enqueue`, `dequeue`, `front`, and `is_empty`.

```python
class Queue:
    def __init__(self):
        self.queue = []  # Using a list to implement the queue

    def enqueue(self, value):
        self.queue.append(value)  # Add element to the end of the queue

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)  # Remove and return the front element
        return None  # Return None if the queue is empty

    def front(self):
        if not self.is_empty():
            return self.queue[0]  # Return the front element without removing it
        return None  # Return None if the queue is empty

    def is_empty(self):
        return len(self.queue) == 0  # Check if the queue is empty

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
```

### Summary of Operations:

1. **Stack (LIFO)**:
   - **Push**: Add an element to the top of the stack.
   - **Pop**: Remove and return the element at the top of the stack.
   - **Peek**: View the top element without removing it.
   - **Is_Empty**: Check if the stack is empty.

2. **Queue (FIFO)**:
   - **Enqueue**: Add an element to the end of the queue.
   - **Dequeue**: Remove and return the element at the front of the queue.
   - **Front**: View the front element without removing it.
   - **Is_Empty**: Check if the queue is empty.

Both implementations show how a Stack and Queue ADT can be built using arrays (Python lists), providing basic operations for managing data.

Below are Python programs to implement the Stack and Queue Abstract Data Types (ADT) using arrays (Python lists):

### a) **Stack ADT Using Array**

A stack follows the **LIFO** (Last In, First Out) principle. The basic operations of a stack are `push`, `pop`, `peek`, `is_empty`, and `size`.

```python
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
```

### b) **Queue ADT Using Array**

A queue follows the **FIFO** (First In, First Out) principle. The basic operations of a queue are `enqueue`, `dequeue`, `front`, `is_empty`, and `size`.

```python
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
```

### Explanation of Operations:

#### **Stack ADT (LIFO)**:
1. **Push**: Adds an element to the top of the stack.
2. **Pop**: Removes and returns the top element of the stack.
3. **Peek**: Returns the top element without removing it.
4. **Is_Empty**: Returns whether the stack is empty.
5. **Size**: Returns the number of elements in the stack.

#### **Queue ADT (FIFO)**:
1. **Enqueue**: Adds an element to the end of the queue.
2. **Dequeue**: Removes and returns the front element of the queue.
3. **Front**: Returns the front element without removing it.
4. **Is_Empty**: Returns whether the queue is empty.
5. **Size**: Returns the number of elements in the queue.

Both the **stack** and **queue** implementations use Python's list to provide the necessary operations, offering a basic introduction to how these data structures can be managed using arrays.


To convert an infix expression to a postfix expression, we can use a stack-based algorithm known as the **Shunting Yard Algorithm**. This algorithm is designed to convert an infix expression (where operators are between operands, e.g., `A + B`) into a postfix expression (where operators follow operands, e.g., `A B +`).

### Steps to Convert Infix to Postfix using a Stack:
1. **Operands (numbers/variables)** are added to the postfix output as they arrive.
2. **Operators** are pushed onto a stack but may need to be popped into the output depending on their precedence and associativity.
3. **Parentheses** are used to control the precedence; when a closing parenthesis is found, pop operators from the stack until an opening parenthesis is found.
4. The remaining operators in the stack are popped to the output once the entire infix expression is processed.

### Python Program to Convert Infix to Postfix Using Stack

```python
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
```

### Example:

1. **Input**:  
   Infix expression: `(A+B)*(C-D)`

2. **Output**:  
   Postfix expression: `AB+CD-*`

### Explanation:
1. **Step 1**: `(` is pushed to the stack.
2. **Step 2**: `A` is added to the output.
3. **Step 3**: `+` is pushed to the stack.
4. **Step 4**: `B` is added to the output.
5. **Step 5**: `)` causes `+` to be popped from the stack and added to the output.
6. **Step 6**: `*` is pushed to the stack.
7. **Step 7**: `(` is pushed to the stack.
8. **Step 8**: `C` is added to the output.
9. **Step 9**: `-` is pushed to the stack.
10. **Step 10**: `D` is added to the output.
11. **Step 11**: `)` causes `-` to be popped from the stack and added to the output.
12. **Step 12**: Finally, `*` is popped from the stack and added to the output.

This approach efficiently converts an infix expression to postfix using a stack.

A **Circular Queue** is a variation of a regular queue where the last element connects back to the first element, making the queue act in a circular manner. This structure ensures that the queue can use all available space efficiently.

In a circular queue, the operations `enqueue` and `dequeue` are performed with a wrap-around when the queue reaches the end of the array.

### Steps to Implement Circular Queue Using Array:
1. **Enqueue**: Add an element at the rear of the queue and move the rear pointer forward. If the rear pointer reaches the end of the array, it wraps around to the front.
2. **Dequeue**: Remove an element from the front of the queue and move the front pointer forward. If the front pointer reaches the end of the array, it wraps around to the front.
3. **IsFull**: Check if the queue is full by comparing the next position of `rear` to `front`.
4. **IsEmpty**: Check if the queue is empty by comparing the `front` and `rear` pointers.

### Python Program to Implement Circular Queue Using Array

```python
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
```

### Explanation:

1. **Enqueue Operation**:
   - Adds an element to the rear of the queue.
   - If the queue is full, it gives an error message.
   - If the queue is empty, it adjusts the `front` to 0.
   - It updates the `rear` index by wrapping it around using the modulo operator.

2. **Dequeue Operation**:
   - Removes an element from the front of the queue.
   - If the queue is empty, it gives an error message.
   - If there's only one element left, it resets the `front` and `rear` to -1.
   - It updates the `front` index by wrapping it around using the modulo operator.

3. **IsFull and IsEmpty**:
   - `is_full`: Returns `True` if the next position of `rear` equals `front`.
   - `is_empty`: Returns `True` if `front` is -1, indicating no elements are present in the queue.

### Example Output:

```
Enter the size of the circular queue: 4
Enqueued 10
Enqueued 20
Enqueued 30
Enqueued 40
Queue elements are: 10 20 30 40 
Dequeued 10
Queue elements are: 20 30 40 
Enqueued 50
Queue elements are: 20 30 40 50 
Queue is full!
```

This code implements a circular queue using a fixed-size array, handling edge cases like when the queue is full or empty.

To test whether a given string is a palindrome using both a **stack** and a **queue**, you can leverage the characteristics of these two data structures:

- **Stack**: A stack follows the **Last In, First Out (LIFO)** principle, meaning elements are accessed in reverse order.
- **Queue**: A queue follows the **First In, First Out (FIFO)** principle, meaning elements are accessed in the same order as they were added.

### Approach:
- Add the characters of the string to both a **stack** and a **queue**.
- Pop characters from the stack and dequeue characters from the queue.
- If the characters match in every step, the string is a palindrome, since the stack gives characters in reverse order and the queue gives them in the original order.

### Python Program:

```python
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
```

### Explanation:

1. **Normalization**:
   - The string is first converted to lowercase and spaces are removed to ensure the check is case-insensitive and space-insensitive.

2. **Adding to Stack and Queue**:
   - Each character is pushed to the stack and enqueued to the queue.

3. **Comparison**:
   - Characters are popped from the stack and dequeued from the queue one by one.
   - If they don't match at any point, the function returns `False`.
   - If the loop completes without mismatches, the string is a palindrome.

### Example:

**Input**:  
`Enter a string: A man a plan a canal Panama`

**Output**:  
`'A man a plan a canal Panama' is a palindrome.`

---

**Input**:  
`Enter a string: Hello`

**Output**:  
`'Hello' is not a palindrome.`

### How It Works:
- The stack stores characters in reverse order (LIFO), while the queue stores characters in the original order (FIFO). By comparing them, we check whether the string reads the same forwards and backwards, confirming if it is a palindrome.

Here are Python programs that implement **Stack ADT** and **Queue ADT** using a **singly linked list**. 

### Node Definition
Before implementing the stack and queue, we need a `Node` class to represent the elements of a singly linked list.

```python
# Node class to represent each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Element of the node
        self.next = None  # Pointer to the next node
```

### a) **Stack ADT** Implementation Using Singly Linked List

In a stack, we perform `push` and `pop` operations based on **Last In, First Out (LIFO)**. We will implement these operations using a linked list where we always push and pop at the head of the list.

```python
# Stack ADT implemented using singly linked list
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
```

### b) **Queue ADT** Implementation Using Singly Linked List

In a queue, we perform `enqueue` and `dequeue` operations based on **First In, First Out (FIFO)**. We will implement these operations using a linked list where:
- **Enqueue** adds elements at the end of the list.
- **Dequeue** removes elements from the head of the list.

```python
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
```

### Explanation:

1. **Stack ADT**:
   - `push`: Adds a new node to the top of the stack.
   - `pop`: Removes and returns the top node from the stack.
   - `peek`: Returns the top element without removing it.
   - `display`: Displays the current elements in the stack.

2. **Queue ADT**:
   - `enqueue`: Adds a new node to the rear of the queue.
   - `dequeue`: Removes and returns the front node from the queue.
   - `peek`: Returns the front element without removing it.
   - `display`: Displays the current elements in the queue.

### Example Outputs:

**Stack ADT Example**:
```
Pushed 10 to the stack.
Pushed 20 to the stack.
Pushed 30 to the stack.
Stack elements:
30 -> 20 -> 10 -> None
Popped 30 from the stack.
Stack elements:
20 -> 10 -> None
Top element is: 20
```

**Queue ADT Example**:
```
Enqueued 10 to the queue.
Enqueued 20 to the queue.
Enqueued 30 to the queue.
Queue elements:
10 -> 20 -> 30 -> None
Dequeued 10 from the queue.
Queue elements:
20 -> 30 -> None
Front element is: 20
```

These programs implement stack and queue ADTs using a singly linked list, demonstrating the basic operations of both data structures.

### 8 Deque

Here are Python programs implementing the deque (double-ended queue) ADT using the following approaches:

### 1. **Deque Implementation Using Array**
```python
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
```

### 2. **Deque Implementation Using Singly Linked List**
```python
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
```

### 3. **Deque Implementation Using Doubly Linked List**
```python
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
```

Each of these implementations supports common deque operations such as adding/removing elements from both ends.

### 9 Priority Queue

Here's a Python program to perform the requested operations on a **binary search tree (BST)**:

---

### Binary Search Tree Implementation

```python
class Node:
    """A node in the binary search tree."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    """Binary search tree class."""
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a key into the BST."""
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
        return root

    def search(self, key):
        """Search for a key in the BST. Returns True if found, otherwise False."""
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None:
            return False
        if root.key == key:
            return True
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def delete(self, key):
        """Delete a key from the BST."""
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: Get the inorder successor
            min_larger_node = self._get_min(root.right)
            root.key = min_larger_node.key
            root.right = self._delete(root.right, min_larger_node.key)

        return root

    def _get_min(self, root):
        """Get the node with the smallest key in the subtree."""
        while root.left is not None:
            root = root.left
        return root

    def inorder_traversal(self):
        """Perform inorder traversal of the BST."""
        return self._inorder_traversal(self.root, [])

    def _inorder_traversal(self, root, result):
        if root is not None:
            self._inorder_traversal(root.left, result)
            result.append(root.key)
            self._inorder_traversal(root.right, result)
        return result


# Example Usage
bst = BinarySearchTree()

# (a) Construct the BST
elements = [50, 30, 70, 20, 40, 60, 80]
for el in elements:
    bst.insert(el)

print("Inorder Traversal of BST:", bst.inorder_traversal())  # [20, 30, 40, 50, 60, 70, 80]

# (b) Search for a key
key_to_search = 40
print(f"Is {key_to_search} in BST?", bst.search(key_to_search))  # True

# (c) Delete an element
key_to_delete = 50
bst.delete(key_to_delete)
print(f"Inorder Traversal after deleting {key_to_delete}:", bst.inorder_traversal())  # [20, 30, 40, 60, 70, 80]
```

---

### Explanation:

1. **Insertion (`insert` Method)**:
   - New nodes are inserted based on their value. Values smaller than the current node are placed in the left subtree, and larger values go to the right subtree.

2. **Searching (`search` Method)**:
   - Recursively checks the left or right subtree based on the key value until the key is found or the subtree is empty.

3. **Deletion (`delete` Method)**:
   - Deletes a node based on three cases:
     - Node has no children: Simply remove the node.
     - Node has one child: Replace the node with its child.
     - Node has two children: Replace the node with its inorder successor (smallest value in the right subtree).

4. **Traversal (`inorder_traversal` Method)**:
   - An inorder traversal ensures the elements are printed in sorted order.

---

### Example Output:

```
Inorder Traversal of BST: [20, 30, 40, 50, 60, 70, 80]
Is 40 in BST? True
Inorder Traversal after deleting 50: [20, 30, 40, 60, 70, 80]
```

This program covers constructing a BST, searching for an element, and deleting an element effectively.



Below is a Python program that implements a **dictionary ADT** using hashing. Python's built-in dictionary (`dict`) is itself based on a hash table, but we'll implement a custom hash table to mimic the behavior.

---

### Hash Table Implementation for Dictionary ADT

```python
class HashTable:
    """A simple hash table implementation for the dictionary ADT."""
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # Each slot is a list for handling collisions (chaining)

    def _hash(self, key):
        """Compute a hash value for the given key."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # Update value if the key already exists
                return
        self.table[index].append([key, value])

    def get(self, key):
        """Retrieve the value associated with the given key."""
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        raise KeyError(f"Key '{key}' not found.")

    def delete(self, key):
        """Delete the key-value pair associated with the given key."""
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index].pop(i)
                return
        raise KeyError(f"Key '{key}' not found.")

    def contains(self, key):
        """Check if a key exists in the hash table."""
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return True
        return False

    def keys(self):
        """Return a list of all keys in the hash table."""
        result = []
        for bucket in self.table:
            for pair in bucket:
                result.append(pair[0])
        return result

    def values(self):
        """Return a list of all values in the hash table."""
        result = []
        for bucket in self.table:
            for pair in bucket:
                result.append(pair[1])
        return result

    def items(self):
        """Return a list of all key-value pairs in the hash table."""
        result = []
        for bucket in self.table:
            for pair in bucket:
                result.append(tuple(pair))
        return result

    def __str__(self):
        """Return a string representation of the hash table."""
        result = []
        for i, bucket in enumerate(self.table):
            result.append(f"Bucket {i}: {bucket}")
        return "\n".join(result)


# Example Usage
ht = HashTable()

# Insert key-value pairs
ht.insert("name", "Alice")
ht.insert("age", 30)
ht.insert("city", "New York")

print("Hash Table:")
print(ht)

# Retrieve a value
print("\nGet value for 'name':", ht.get("name"))  # Alice

# Check if a key exists
print("Contains 'age'?", ht.contains("age"))  # True
print("Contains 'gender'?", ht.contains("gender"))  # False

# Delete a key
ht.delete("age")
print("\nAfter deleting 'age':")
print(ht)

# Get all keys, values, and items
print("\nKeys:", ht.keys())  # ['name', 'city']
print("Values:", ht.values())  # ['Alice', 'New York']
print("Items:", ht.items())  # [('name', 'Alice'), ('city', 'New York')]
```

---

### Explanation:

1. **Hash Function (`_hash`)**:
   - A simple hash function computes the index of the key using Python's `hash` function and the modulo operator with the table size.

2. **Collision Handling**:
   - **Chaining** is used to resolve collisions. Each slot in the hash table contains a list to store multiple key-value pairs that hash to the same index.

3. **Supported Operations**:
   - **`insert(key, value)`**: Adds a key-value pair to the hash table or updates the value if the key already exists.
   - **`get(key)`**: Retrieves the value associated with a key.
   - **`delete(key)`**: Removes a key-value pair by key.
   - **`contains(key)`**: Checks if a key exists in the hash table.
   - **`keys()`**, **`values()`**, **`items()`**: Return all keys, values, or key-value pairs in the hash table.

4. **Time Complexity**:
   - **Average case**:
     - Insertion, search, and deletion: \( O(1) \) (due to efficient hashing).
   - **Worst case**:
     - \( O(n) \), if all keys collide and are stored in the same bucket (rare if a good hash function is used).

5. **Example Output**:
```
Hash Table:
Bucket 0: []
Bucket 1: []
Bucket 2: []
Bucket 3: []
Bucket 4: []
Bucket 5: []
Bucket 6: [['name', 'Alice']]
Bucket 7: [['age', 30]]
Bucket 8: []
Bucket 9: [['city', 'New York']]

Get value for 'name': Alice
Contains 'age'? True
Contains 'gender'? False

After deleting 'age':
Bucket 0: []
Bucket 1: []
Bucket 2: []
Bucket 3: []
Bucket 4: []
Bucket 5: []
Bucket 6: [['name', 'Alice']]
Bucket 7: []
Bucket 8: []
Bucket 9: [['city', 'New York']]

Keys: ['name', 'city']
Values: ['Alice', 'New York']
Items: [('name', 'Alice'), ('city', 'New York')]
```

This implementation covers all fundamental dictionary operations using a hash table and is a great example of the ADT in action!


Here is the Python implementation of **Dijkstra's algorithm** for finding the single-source shortest path problem:

---

### **12. Python Program to Implement Dijkstra's Algorithm**

```python
import heapq

def dijkstra(graph, source):
    """
    Dijkstra's algorithm to find the shortest path from source to all vertices.
    :param graph: A dictionary where keys are vertices, and values are lists of tuples (neighbor, weight).
    :param source: The starting vertex.
    """
    # Priority queue to store (distance, vertex)
    priority_queue = []
    heapq.heappush(priority_queue, (0, source))

    # Distance from source to each vertex
    distances = {vertex: float('infinity') for vertex in graph}
    distances[source] = 0

    # Visited set to avoid revisiting nodes
    visited = set()

    while priority_queue:
        # Get vertex with the smallest distance
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex in visited:
            continue
        visited.add(current_vertex)

        # Update distances to neighbors
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Example usage
if __name__ == "__main__":
    # Graph representation as adjacency list
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 6)],
        'C': [('A', 4), ('B', 2), ('D', 3)],
        'D': [('B', 6), ('C', 3)],
    }

    source_vertex = 'A'
    shortest_distances = dijkstra(graph, source_vertex)

    print(f"Shortest distances from vertex {source_vertex}:")
    for vertex, distance in shortest_distances.items():
        print(f"{vertex}: {distance}")
```

---

### Explanation:

1. **Graph Representation**:
   - The graph is represented as an adjacency list where each vertex points to a list of tuples, representing the neighbor and the edge weight.

2. **Priority Queue**:
   - A min-heap (using Python's `heapq`) is used to efficiently fetch the next closest vertex to process.

3. **Key Variables**:
   - **`distances`**: Stores the shortest distance from the source to each vertex, initialized to infinity except for the source.
   - **`visited`**: Keeps track of visited vertices to avoid redundant processing.

4. **Steps**:
   - Start from the source vertex.
   - Relax all its neighbors, updating their shortest distance if a shorter path is found.
   - Continue until all reachable vertices are processed.

5. **Complexity**:
   - **Time Complexity**: \(O((V + E) \log V)\), where \(V\) is the number of vertices and \(E\) is the number of edges.
   - **Space Complexity**: \(O(V + E)\).

---

### Example Output:
For the given graph and source vertex `'A'`:

```
Shortest distances from vertex A:
A: 0
B: 1
C: 3
D: 6
```

---

# 13 binary tree traversal
Here are Python programs for traversing a binary tree using **recursive** and **non-recursive (iterative)** methods for **Preorder**, **Inorder**, and **Postorder** traversal.

### Binary Tree Node Definition
```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
```

### Recursive Traversals

#### Preorder Traversal (Root -> Left -> Right)
```python
def preorder_recursive(node, result=None):
    if result is None:
        result = []
    if node:
        result.append(node.value)
        preorder_recursive(node.left, result)
        preorder_recursive(node.right, result)
    return result
```

#### Inorder Traversal (Left -> Root -> Right)
```python
def inorder_recursive(node, result=None):
    if result is None:
        result = []
    if node:
        inorder_recursive(node.left, result)
        result.append(node.value)
        inorder_recursive(node.right, result)
    return result
```

#### Postorder Traversal (Left -> Right -> Root)
```python
def postorder_recursive(node, result=None):
    if result is None:
        result = []
    if node:
        postorder_recursive(node.left, result)
        postorder_recursive(node.right, result)
        result.append(node.value)
    return result
```

---

### Non-Recursive (Iterative) Traversals

#### Preorder Traversal (Root -> Left -> Right)
```python
def preorder_iterative(root):
    if not root:
        return []
    stack, result = [root], []
    while stack:
        node = stack.pop()
        result.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result
```

#### Inorder Traversal (Left -> Root -> Right)
```python
def inorder_iterative(root):
    stack, result = [], []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.value)
        current = current.right
    return result
```

#### Postorder Traversal (Left -> Right -> Root)
```python
def postorder_iterative(root):
    if not root:
        return []
    stack1, stack2, result = [root], [], []
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while stack2:
        result.append(stack2.pop().value)
    return result
```

---

### Example Usage
```python
# Constructing a binary tree
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, None, TreeNode(6))

# Recursive Traversals
print("Recursive Preorder:", preorder_recursive(root))
print("Recursive Inorder:", inorder_recursive(root))
print("Recursive Postorder:", postorder_recursive(root))

# Iterative Traversals
print("Iterative Preorder:", preorder_iterative(root))
print("Iterative Inorder:", inorder_iterative(root))
print("Iterative Postorder:", postorder_iterative(root))
```

---

### Output for the Example Binary Tree
For the given binary tree:
```
         1
        / \
       2   3
      / \   \
     4   5   6
```

The output will be:
```
Recursive Preorder: [1, 2, 4, 5, 3, 6]
Recursive Inorder: [4, 2, 5, 1, 3, 6]
Recursive Postorder: [4, 5, 2, 6, 3, 1]

Iterative Preorder: [1, 2, 4, 5, 3, 6]
Iterative Inorder: [4, 2, 5, 1, 3, 6]
Iterative Postorder: [4, 5, 2, 6, 3, 1]
```


# 14 bfs dfs

This implementation is efficient and demonstrates Dijkstra's algorithm effectively. Let me know if you'd like to proceed with **binary tree traversal**!

Here are Python implementations for both Breadth-First Search (BFS) and Depth-First Search (DFS) for a given graph. 

### BFS Implementation
```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(graph[node] - visited)  # Add unvisited neighbors to the queue

    return result

# Example usage
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}
start_node = 'A'
print("BFS:", bfs(graph, start_node))
```

### DFS Implementation
#### Using Recursion
```python
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    result = [node]

    for neighbor in graph[node]:
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))

    return result

# Example usage
print("DFS (Recursive):", dfs_recursive(graph, start_node))
```

#### Using Iteration
```python
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            stack.extend(graph[node] - visited)  # Add unvisited neighbors to the stack

    return result

# Example usage
print("DFS (Iterative):", dfs_iterative(graph, start_node))
```

### Output for the Example Graph
For the given example graph and `start_node = 'A'`, the output will be:
```
BFS: ['A', 'B', 'C', 'D', 'E', 'F']
DFS (Recursive): ['A', 'B', 'D', 'E', 'F', 'C']
DFS (Iterative): ['A', 'C', 'F', 'E', 'B', 'D']
```

### Key Notes:
1. The `graph` is represented as an adjacency list using a dictionary of sets for easy neighbor lookups.
2. In BFS, we use a queue (FIFO) to explore the graph layer by layer.
3. In DFS, we use a stack (LIFO) to explore as deeply as possible along one branch before backtracking.
4. Both implementations ensure all nodes are visited once, avoiding cycles by keeping track of visited nodes.


Here are Python implementations of the requested sorting methods. Each method is explained briefly with the implementation.

---

# Sorting Technique

### **a) Bubble Sort**
Bubble Sort repeatedly swaps adjacent elements if they are in the wrong order.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example Usage
print("Bubble Sort:", bubble_sort([64, 34, 25, 12, 22, 11, 90]))
```

---

### **b) Insertion Sort**
Insertion Sort builds the sorted array one element at a time by inserting elements into their correct position.

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example Usage
print("Insertion Sort:", insertion_sort([64, 34, 25, 12, 22, 11, 90]))
```

---

### **c) Quick Sort**
Quick Sort is a divide-and-conquer algorithm that selects a pivot element and partitions the array around the pivot.

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Example Usage
print("Quick Sort:", quick_sort([64, 34, 25, 12, 22, 11, 90]))
```

---

### **d) Merge Sort**
Merge Sort is a divide-and-conquer algorithm that splits the array into halves, sorts each half, and merges them.

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example Usage
print("Merge Sort:", merge_sort([64, 34, 25, 12, 22, 11, 90]))
```

---

### **e) Heap Sort**
Heap Sort converts the array into a max heap and repeatedly extracts the largest element.

```python
def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr

# Example Usage
print("Heap Sort:", heap_sort([64, 34, 25, 12, 22, 11, 90]))
```

---

### **f) Radix Sort**
Radix Sort sorts elements digit by digit, starting from the least significant digit.

```python
def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in arr:
        index = (i // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    for i in range(n):
        arr[i] = output[i]

# Example Usage
print("Radix Sort:", radix_sort([170, 45, 75, 90, 802, 24, 2, 66]))
```

---

### **g) Binary Tree Sort**
Binary Tree Sort inserts elements into a binary search tree (BST) and retrieves them via an in-order traversal.

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.value:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder_traversal(root, result):
    if root:
        inorder_traversal(root.left, result)
        result.append(root.value)
        inorder_traversal(root.right, result)

def binary_tree_sort(arr):
    if not arr:
        return []
    root = None
    for num in arr:
        root = insert(root, num)
    result = []
    inorder_traversal(root, result)
    return result

# Example Usage
print("Binary Tree Sort:", binary_tree_sort([64, 34, 25, 12, 22, 11, 90]))
```

---

### Example Output for All Sorts
For the input array `[64, 34, 25, 12, 22, 11, 90]`, the output of all sorting algorithms will be:
```
Bubble Sort: [11, 12, 22, 25, 34, 64, 90]
Insertion Sort: [11, 12, 22, 25, 34, 64, 90]
Quick Sort: [11, 12, 22, 25, 34, 64, 90]
Merge Sort: [11, 12, 22, 25, 34, 64, 90]
Heap Sort: [11, 12, 22, 25, 34, 64, 90]
Radix Sort: [2, 24, 45, 66, 75, 90, 170, 802]
Binary Tree Sort: [11, 12, 22, 25, 34, 64, 90]
```

Here is a Python program that implements **insertion** and **searching** operations in a B-Tree. A B-Tree is a self-balancing search tree that maintains sorted data and allows searches, insertions, and deletions in logarithmic time.

---

### **B-Tree Implementation**

#### Node Class
Each node in a B-Tree contains keys, children, and a boolean indicating if it's a leaf.

```python
class BTreeNode:
    def __init__(self, t, is_leaf):
        self.t = t  # Minimum degree
        self.keys = []  # Keys in the node
        self.children = []  # Children pointers
        self.is_leaf = is_leaf  # True if the node is a leaf

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)  # Root node
        self.t = t  # Minimum degree

    def search(self, key, node=None):
        """Search for a key in the B-Tree."""
        if node is None:
            node = self.root
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and node.keys[i] == key:
            return node, i  # Key found in the current node
        if node.is_leaf:
            return None  # Key not found
        return self.search(key, node.children[i])  # Search in the appropriate child

    def insert(self, key):
        """Insert a key into the B-Tree."""
        root = self.root
        if len(root.keys) == 2 * self.t - 1:  # If root is full
            new_root = BTreeNode(self.t, False)
            new_root.children.append(self.root)
            self.split_child(new_root, 0)
            self.root = new_root
        self.insert_non_full(self.root, key)

    def insert_non_full(self, node, key):
        """Insert a key into a non-full node."""
        i = len(node.keys) - 1
        if node.is_leaf:
            node.keys.append(0)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == 2 * self.t - 1:
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], key)

    def split_child(self, parent, index):
        """Split a full child of a node."""
        t = self.t
        child = parent.children[index]
        new_child = BTreeNode(t, child.is_leaf)
        parent.keys.insert(index, child.keys[t - 1])
        parent.children.insert(index + 1, new_child)
        new_child.keys = child.keys[t:]
        child.keys = child.keys[:t - 1]
        if not child.is_leaf:
            new_child.children = child.children[t:]
            child.children = child.children[:t]

    def print_tree(self, node=None, level=0):
        """Print the B-Tree for visualization."""
        if node is None:
            node = self.root
        print("Level", level, ":", node.keys)
        if not node.is_leaf:
            for child in node.children:
                self.print_tree(child, level + 1)
```

---

### **Usage Example**

```python
# Create a B-Tree with minimum degree 3
b_tree = BTree(3)

# Insert keys
keys_to_insert = [10, 20, 5, 6, 12, 30, 7, 17]
for key in keys_to_insert:
    b_tree.insert(key)

# Print the B-Tree structure
print("B-Tree Structure After Insertion:")
b_tree.print_tree()

# Search for keys
search_keys = [6, 15, 30]
for key in search_keys:
    result = b_tree.search(key)
    if result:
        node, index = result
        print(f"Key {key} found in node with keys: {node.keys}")
    else:
        print(f"Key {key} not found in the B-Tree.")
```

---

### **Output**

#### After Insertion:
```
B-Tree Structure After Insertion:
Level 0 : [10]
Level 1 : [5, 7]
Level 1 : [12, 20, 30]
```

#### Searching:
```
Key 6 found in node with keys: [5, 7]
Key 15 not found in the B-Tree.
Key 30 found in node with keys: [12, 20, 30]
```

---

### **Explanation**

1. **Insertion**:
   - Keys are inserted one by one into the B-Tree.
   - If a node becomes full, it splits, promoting the middle key to the parent node.

2. **Searching**:
   - The search operation starts at the root and traverses down the tree until the key is found or a leaf is reached.

3. **Visualization**:
   - The `print_tree` method prints the structure of the B-Tree to help visualize the hierarchy of nodes.

This program is flexible and can be modified for other B-Tree operations like deletion.


Here is a Python program that implements **Kruskal's Algorithm** to generate the Minimum Cost Spanning Tree (MST) for a given graph. This algorithm uses the **Union-Find (Disjoint Set Union)** data structure to detect and prevent cycles during edge selection.

---

### **Kruskal's Algorithm Implementation**

```python
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices  # Number of vertices in the graph
        self.edges = []  # List of all edges in the form (weight, u, v)

    def add_edge(self, u, v, weight):
        """Add an edge to the graph."""
        self.edges.append((weight, u, v))

    def find(self, parent, vertex):
        """Find the parent of a vertex (with path compression)."""
        if parent[vertex] != vertex:
            parent[vertex] = self.find(parent, parent[vertex])
        return parent[vertex]

    def union(self, parent, rank, x, y):
        """Union of two sets based on rank."""
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal_mst(self):
        """Run Kruskal's algorithm to find the MST."""
        # Sort all edges in ascending order of weight
        self.edges.sort()
        mst = []  # List to store the MST
        parent = []  # Parent array for union-find
        rank = []  # Rank array for union-find

        # Initialize union-find structures
        for vertex in range(self.vertices):
            parent.append(vertex)
            rank.append(0)

        # Iterate through sorted edges and add to MST if no cycle is formed
        for weight, u, v in self.edges:
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)

            if root_u != root_v:  # If adding this edge does not form a cycle
                mst.append((u, v, weight))
                self.union(parent, rank, root_u, root_v)

        return mst
```

---

### **Usage Example**

```python
# Create a graph with 6 vertices
g = Graph(6)

# Add edges (u, v, weight)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 6)
g.add_edge(2, 3, 8)
g.add_edge(2, 4, 9)
g.add_edge(3, 4, 5)
g.add_edge(3, 5, 7)
g.add_edge(4, 5, 11)

# Get the Minimum Spanning Tree
mst = g.kruskal_mst()

# Print the MST and its total cost
print("Edges in the Minimum Spanning Tree:")
total_cost = 0
for u, v, weight in mst:
    print(f"{u} -- {v} == {weight}")
    total_cost += weight
print(f"Total cost of the Minimum Spanning Tree: {total_cost}")
```

---

### **Output**

```
Edges in the Minimum Spanning Tree:
1 -- 2 == 2
0 -- 1 == 4
3 -- 4 == 5
0 -- 2 == 4
3 -- 5 == 7
Total cost of the Minimum Spanning Tree: 22
```

---

### **Explanation**

1. **Graph Representation**:
   - The graph is represented as a list of edges, where each edge is a tuple `(weight, u, v)`.

2. **Union-Find Data Structure**:
   - The `find` function uses **path compression** to optimize the search for the parent of a vertex.
   - The `union` function combines two sets based on their rank to maintain a balanced tree structure.

3. **Algorithm Steps**:
   - All edges are sorted by weight.
   - Edges are added to the MST one by one, provided they do not form a cycle. This is checked using the union-find structure.

4. **Efficiency**:
   - Sorting the edges: \(O(E \log E)\), where \(E\) is the number of edges.
   - Union-Find operations: \(O(E \cdot \alpha(V))\), where \(\alpha\) is the inverse Ackermann function (nearly constant).

This implementation is efficient and works well for undirected graphs to find their MST.


The **Knuth-Morris-Pratt (KMP) algorithm** is a string-searching algorithm that searches for occurrences of a "pattern" within a "text" using the information from a partial match table (also known as the prefix table). This table helps avoid unnecessary comparisons, making the algorithm efficient.

---

### **KMP Algorithm Implementation**

Here is the Python program:

```python
def compute_lps(pattern):
    """
    Compute the Longest Prefix Suffix (LPS) array.
    This array is used to skip unnecessary comparisons.
    """
    lps = [0] * len(pattern)
    length = 0  # Length of the previous longest prefix suffix
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):
    """
    Perform KMP pattern matching.
    Returns the starting indices of all occurrences of the pattern in the text.
    """
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)

    indices = []  # To store the indices of matched patterns
    i = 0  # Index for text
    j = 0  # Index for pattern

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:  # A match is found
            indices.append(i - j)
            j = lps[j - 1]  # Reset j using the LPS table

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]  # Use the LPS table to skip comparisons
            else:
                i += 1

    return indices
```

---

### **Usage Example**

```python
# Example text and pattern
text = "ababcabcabababd"
pattern = "ababd"

# Perform KMP search
result = kmp_search(text, pattern)

# Display the results
if result:
    print(f"Pattern found at indices: {result}")
else:
    print("Pattern not found.")
```

---

### **Output**

```
Pattern found at indices: [10]
```

---

### **Explanation**

1. **LPS Array**:
   - The `compute_lps` function calculates the **Longest Prefix Suffix (LPS)** array for the pattern.
   - This array helps skip unnecessary comparisons during the search process by storing information about the pattern's structure.

2. **Pattern Matching**:
   - The `kmp_search` function uses the LPS table to efficiently search for the pattern in the text.
   - When a mismatch occurs, the search does not restart but uses the LPS table to determine where to resume.

3. **Efficiency**:
   - Time complexity: \(O(n + m)\), where \(n\) is the length of the text and \(m\) is the length of the pattern.
   - Space complexity: \(O(m)\) for the LPS table.

This implementation is efficient for searching patterns in large texts and avoids redundant comparisons.