# Quick Sort with middle element pivot and step display

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        print("After partition with pivot =", arr[pivot_index], ":", arr)

        # Recursively sort sub-arrays
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    # Choose middle element as pivot
    mid = (low + high) // 2
    pivot = arr[mid]

    left = low
    right = high

    while True:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left >= right:
            return right
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


# Test Case 1
arr1 = [19, 72, 35, 46, 58, 91, 22, 31]
print("Input:", arr1)
quick_sort(arr1, 0, len(arr1) - 1)
print("Final Sorted Output:", arr1)

# Test Case 2
arr2 = [31, 23, 35, 27, 11, 21, 15, 28]
print("\nInput:", arr2)
quick_sort(arr2, 0, len(arr2) - 1)
print("Final Sorted Output:", arr2)

# Test Case 3
arr3 = [22, 34, 25, 36, 43, 67, 52, 13, 65, 17]
print("\nInput:", arr3)
quick_sort(arr3, 0, len(arr3) - 1)
print("Final Sorted Output:", arr3)
