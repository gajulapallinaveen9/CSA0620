def processList(nums):
    if not nums:
        return "The list is empty"
    sorted_nums = sorted(nums)
    return sorted_nums[-1]
nums1 = []
print(processList(nums1))
nums2 = [5]
print(processList(nums2))
nums3 = [3, 3, 3, 3, 3]
print(processList(nums3))

