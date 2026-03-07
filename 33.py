# Merge Sort with comparison counter

comparison_count = 0  # global counter

def merge_sort(arr):
    global comparison_count
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
            comparison_count += 1  # count each comparison
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
comparison_count = 0
arr1 = [12, 4, 78, 23, 45, 67, 89, 1]
sorted_arr1 = merge_sort(arr1)
print("Input:", [12, 4, 78, 23, 45, 67, 89, 1])
print("Sorted Output:", sorted_arr1)
print("Comparisons:", comparison_count)

# Test Case 2
comparison_count = 0
arr2 = [38, 27, 43, 3, 9, 82, 10]
sorted_arr2 = merge_sort(arr2)
print("\nInput:", [38, 27, 43, 3, 9, 82, 10])
print("Sorted Output:", sorted_arr2)
print("Comparisons:", comparison_count)
