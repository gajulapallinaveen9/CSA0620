# Median of Medians algorithm to find k-th smallest element

def partition(arr, low, high, pivot_index):
    pivot_value = arr[pivot_index]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # move pivot to end
    store_index = low
    for i in range(low, high):
        if arr[i] < pivot_value:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1
    arr[store_index], arr[high] = arr[high], arr[store_index]  # move pivot to final place
    return store_index

def select(arr, low, high, k):
    while True:
        if low == high:
            return arr[low]

        # Divide into groups of 5 and find medians
        medians = []
        i = low
        while i <= high:
            group = arr[i:min(i+5, high+1)]
            group.sort()
            medians.append(group[len(group)//2])
            i += 5

        # Find median of medians recursively
        if len(medians) == 1:
            pivot_value = medians[0]
        else:
            pivot_value = select(medians, 0, len(medians)-1, len(medians)//2)

        # Find pivot index
        pivot_index = arr.index(pivot_value, low, high+1)

        # Partition around pivot
        pivot_index = partition(arr, low, high, pivot_index)

        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            high = pivot_index - 1
        else:
            low = pivot_index + 1


def kth_smallest(arr, k):
    # k is 1-based index
    return select(arr, 0, len(arr)-1, k-1)


# Test Case 1
arr1 = [12, 3, 5, 7, 19]
k1 = 2
print("Input:", arr1, "k =", k1)
print("Output:", kth_smallest(arr1, k1))  # Expected 5

# Test Case 2
arr2 = [12, 3, 5, 7, 4, 19, 26]
k2 = 3
print("\nInput:", arr2, "k =", k2)
print("Output:", kth_smallest(arr2, k2))  # Expected 5

# Test Case 3
arr3 = [1,2,3,4,5,6,7,8,9,10]
k3 = 6
print("\nInput:", arr3, "k =", k3)
print("Output:", kth_smallest(arr3, k3))  # Expected 6
