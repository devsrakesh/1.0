import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        """Check if the priority queue is empty."""
        return len(self.heap) == 0

    def insert(self, priority, item):
        """
        Insert an item with a given priority.
        Lower priority values are dequeued first (min-heap behavior).
        """
        heapq.heappush(self.heap, (priority, item))

    def remove(self):
        """
        Remove and return the item with the highest priority (lowest priority value).
        Raises IndexError if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Priority Queue is empty")
        return heapq.heappop(self.heap)[1]

    def peek(self):
        """
        Return the item with the highest priority without removing it.
        Raises IndexError if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Priority Queue is empty")
        return self.heap[0][1]

    def __str__(self):
        """Return a string representation of the priority queue."""
        return str([(priority, item) for priority, item in self.heap])


# Example Usage
pq = PriorityQueue()
pq.insert(3, "Task C")  # Lower priority numbers indicate higher priority
pq.insert(1, "Task A")
pq.insert(2, "Task B")

print("Priority Queue:", pq)  # [(1, 'Task A'), (3, 'Task C'), (2, 'Task B')]

print("Peek:", pq.peek())  # Task A
print("Removed:", pq.remove())  # Task A
print("Priority Queue after removal:", pq)  # [(2, 'Task B'), (3, 'Task C')]

pq.insert(0, "Task D")
print("Priority Queue after inserting Task D:", pq)  # [(0, 'Task D'), (3, 'Task C'), (2, 'Task B')]
