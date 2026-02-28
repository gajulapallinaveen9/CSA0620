def unique_elements(nums):
    # Convert list to a set to remove duplicates
    unique = list(set(nums))
    return unique


# Test Cases

# 1. Some Duplicate Elements
print(unique_elements([3, 7, 3, 5, 2, 5, 9, 2]))  
# Output: [2, 3, 5, 7, 9] (order may vary)

# 2. Negative and Positive Numbers
print(unique_elements([-1, 2, -1, 3, 2, -2]))     
# Output: [-1, 2, 3, -2] (order may vary)

# 3. List with Large Numbers
print(unique_elements([1000000, 999999, 1000000]))  
# Output: [1000000, 999999] (order may vary)
