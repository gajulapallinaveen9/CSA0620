def max_absolute_value(arr):
    # Find maximum absolute value in one pass
    return max(abs(x) for x in arr)

# Test Cases
print(max_absolute_value([1, 2, 3, 4, 5]))       # Output: 5
print(max_absolute_value([7, 7, 7, 7, 7]))       # Output: 7
print(max_absolute_value([-10, 2, 3, -4, 5]))    # Output: 10
