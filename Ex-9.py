def binary_search(arr, key):
    # First, ensure the array is sorted
    arr.sort()
    
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == key:
            return mid  # return position (0-indexed)
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # not found


# Test Case 1
X = [3, 4, 6, -9, 10, 8, 9, 30]
KEY = 10
pos = binary_search(X, KEY)
if pos != -1:
    print(f"Element {KEY} is found at position {pos}")
else:
    print(f"Element {KEY} is not found")

# Test Case 2
KEY = 100
pos = binary_search(X, KEY)
if pos != -1:
    print(f"Element {KEY} is found at position {pos}")
else:
    print(f"Element {KEY} is not found")
