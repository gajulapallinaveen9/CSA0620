def process_list(nums):
    # Handle empty list case
    if not nums:
        return None  # or return "List is empty"
    
    # Sort the list using efficient built-in sort (Timsort)
    nums.sort()
    
    # The maximum element will be the last element in the sorted list
    return nums[-1]


# Test Cases

# 1. Empty List
print(process_list([]))  # Output: None

# 2. Single Element List
print(process_list([5]))  # Output: 5

# 3. All Elements are the Same
print(process_list([3, 3, 3, 3, 3]))  # Output: 3
