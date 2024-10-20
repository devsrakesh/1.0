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
