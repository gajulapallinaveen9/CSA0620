def count_pairs(nums, k):
    n = len(nums)
    count = 0
    
    # Loop through all pairs (i, j)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j] and (i * j) % k == 0:
                count += 1
    
    return count


# Example 1
nums1 = [3,1,2,2,2,1,3]
k1 = 2
print(count_pairs(nums1, k1))  # Output: 4

# Example 2
nums2 = [1,2,3,4]
k2 = 1
print(count_pairs(nums2, k2))  # Output: 0
