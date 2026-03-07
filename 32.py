def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive calls
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge the two halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy remaining elements of left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy remaining elements of right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr


# Test Case 1
arr1 = [31, 23, 35, 27, 11, 21, 15, 28]
print("Input:", arr1)
print("Output:", merge_sort(arr1))

# Test Case 2
arr2 = [22, 34, 25, 36, 43, 67, 52, 13, 65, 17]
print("\nInput:", arr2)
print("Output:", merge_sort(arr2))
