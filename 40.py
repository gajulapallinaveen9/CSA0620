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

        # Step 1: Divide into groups of 5 and find medians
        medians = []
        i = low
        while i <= high:
            group = arr[i:min(i+5, high+1)]
            group.sort()
            medians.append(group[len(group)//2])
            i += 5

        # Step 2: Find median of medians recursively
        if len(medians) == 1:
            pivot_value = medians[0]
        else:
            pivot_value = select(medians, 0, len(medians)-1, len(medians)//2)

        # Step 3: Partition around pivot
        pivot_index = arr.index(pivot_value, low, high+1)
        pivot_index = partition(arr, low, high, pivot_index)

        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            high = pivot_index - 1
        else:
            low = pivot_index + 1

def median_of_medians(arr, k):
    # k is 1-based index
    return select(arr, 0, len(arr)-1, k-1)


# Test Case 1
arr1 = [1,2,3,4,5,6,7,8,9,10]
k1 = 6
print("Input:", arr1, "k =", k1)
print("Output:", median_of_medians(arr1, k1))  # Expected 6

# Test Case 2
arr2 = [23,17,31,44,55,21,20,18,19,27]
k2 = 5
print("\nInput:", arr2, "k =", k2)
print("Output:", median_of_medians(arr2, k2))  # Expected 5th smallest = 21
