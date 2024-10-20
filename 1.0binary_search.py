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
