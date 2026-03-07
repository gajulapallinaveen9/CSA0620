# Program to find minimum and maximum in an array

def find_min_max(arr):
    minimum = min(arr)
    maximum = max(arr)
    return minimum, maximum

# Test Case 1
arr1 = [2, 4, 6, 8, 10, 12, 14, 18]
min_val, max_val = find_min_max(arr1)
print("Input:", arr1)
print("Output: Min =", min_val, ", Max =", max_val)

# Test Case 2
arr2 = [11, 13, 15, 17, 19, 21, 23, 35, 37]
min_val, max_val = find_min_max(arr2)
print("\nInput:", arr2)
print("Output: Min =", min_val, ", Max =", max_val)

# Test Case 3
arr3 = [22, 34, 35, 36, 43, 67, 12, 13, 15, 17]
min_val, max_val = find_min_max(arr3)
print("\nInput:", arr3)
print("Output: Min =", min_val, ", Max =", max_val)
