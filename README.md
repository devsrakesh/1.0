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