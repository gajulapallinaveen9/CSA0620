def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Test Cases
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))   # Output: [11, 12, 22, 25, 34, 64, 90]
print(bubble_sort([5, 1, 4, 2, 8]))                # Output: [1, 2, 4, 5, 8]
print(bubble_sort([]))                             # Output: []
print(bubble_sort([3]))                            # Output: [3]
