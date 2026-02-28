def sumCounts(nums):
    n = len(nums)
    total = 0

    for i in range(n):
        seen = set()
        for j in range(i, n):
            seen.add(nums[j])
            total += len(seen) ** 2

    return total


# Example usage
print(sumCounts([1, 2, 1]))  
print(sumCounts([1, 1]))
