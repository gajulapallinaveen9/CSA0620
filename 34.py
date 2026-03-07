# Quick Sort with step-by-step display

def quick_sort(arr, low, high):
    if low < high:
        # Partition the array
        pivot_index = partition(arr, low, high)
        print("After partition with pivot =", arr[pivot_index], ":", arr)

        # Recursively sort sub-arrays
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    pivot = arr[low]  # first element as pivot
    left = low + 1
    right = high

    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1
        if left > right:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]

    arr[low], arr[right] = arr[right], arr[low]
    return right


# Test Case 1
arr1 = [10, 16, 8, 12, 15, 6, 3, 9, 5]
print("Input:", arr1)
quick_sort(arr1, 0, len(arr1) - 1)
print("Final Sorted Output:", arr1)

# Test Case 2
arr2 = [12, 4, 78, 23, 45, 67, 89, 1]
print("\nInput:", arr2)
quick_sort(arr2, 0, len(arr2) - 1)
print("Final Sorted Output:", arr2)

# Test Case 3
arr3 = [38, 27, 43, 3, 9, 82, 10]
print("\nInput:", arr3)
quick_sort(arr3, 0, len(arr3) - 1)
print("Final Sorted Output:", arr3)
