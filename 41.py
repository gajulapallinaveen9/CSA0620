from itertools import combinations
import bisect

# function to generate all subset sums
def subset_sums(arr):
    sums = []
    n = len(arr)
    for r in range(n + 1):
        for comb in combinations(arr, r):
            sums.append(sum(comb))
    return sums

def meet_in_middle(arr, target):
    n = len(arr)

    # divide array into two halves
    left = arr[:n//2]
    right = arr[n//2:]

    # generate subset sums
    left_sums = subset_sums(left)
    right_sums = subset_sums(right)

    # sort right sums
    right_sums.sort()

    closest = None
    min_diff = float('inf')

    # search best pair
    for s in left_sums:
        remaining = target - s
        pos = bisect.bisect_left(right_sums, remaining)

        if pos < len(right_sums):
            total = s + right_sums[pos]
            diff = abs(target - total)
            if diff < min_diff:
                min_diff = diff
                closest = total

        if pos > 0:
            total = s + right_sums[pos-1]
            diff = abs(target - total)
            if diff < min_diff:
                min_diff = diff
                closest = total

    return closest


# Test Case A
set1 = [45, 34, 4, 12, 5, 2]
target1 = 42
print("Set:", set1)
print("Target:", target1)
print("Closest Subset Sum:", meet_in_middle(set1, target1))

print()

# Test Case B
set2 = [1, 3, 2, 7, 4, 6]
target2 = 10
print("Set:", set2)
print("Target:", target2)
print("Closest Subset Sum:", meet_in_middle(set2, target2))
