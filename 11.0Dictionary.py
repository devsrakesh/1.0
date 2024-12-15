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
