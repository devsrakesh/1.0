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
