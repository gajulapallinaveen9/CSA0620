def findPeakElement(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        # Compare mid element with its right neighbor
        if nums[mid] > nums[mid + 1]:
            # Peak lies on the left side (including mid)
            right = mid
        else:
            # Peak lies on the right side
            left = mid + 1
    
    # At the end, left == right, pointing to a peak element
    return left


# Example usage:
print(findPeakElement([1, 2, 3, 1]))        # Output: 2
print(findPeakElement([1, 2, 1, 3, 5, 6, 4]))  # Output: 5 (or 1, both valid)
