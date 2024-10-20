# Non-Recursive Linear Search
def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index  
    return -1  

# Example usage:
arr = [10, 23, 45, 70, 11, 15]
target = 70
result = linear_search(arr, target)
print(f"Non-Recursive Linear Search: Target found at index {result}")
