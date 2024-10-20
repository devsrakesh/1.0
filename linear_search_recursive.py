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
