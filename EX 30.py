def find_min_max(arr, low, high):
    # Base case: only one element
    if low == high:
        return arr[low], arr[low]
    
    # Base case: two elements
    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    
    # Divide the array into two halves
    mid = (low + high) // 2
    min1, max1 = find_min_max(arr, low, mid)
    min2, max2 = find_min_max(arr, mid+1, high)
    
    # Combine results
    return min(min1, min2), max(max1, max2)


# -------------------------------
# Test Cases
# -------------------------------

# Test Case 1
arr1 = [5,7,3,4,9,12,6,2]
min_val1, max_val1 = find_min_max(arr1, 0, len(arr1)-1)
print("Test Case 1: Min =", min_val1, "Max =", max_val1)

# Test Case 2
arr2 = [1,3,5,7,9,11,13,15,17]
min_val2, max_val2 = find_min_max(arr2, 0, len(arr2)-1)
print("Test Case 2: Min =", min_val2, "Max =", max_val2)

# Test Case 3
arr3 = [22,34,35,36,43,67,12,13,15,17]
min_val3, max_val3 = find_min_max(arr3, 0, len(arr3)-1)
print("Test Case 3: Min =", min_val3, "Max =", max_val3)
