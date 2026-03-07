from itertools import combinations

# function to generate subset sums
def subset_sums(arr):
    sums = []
    n = len(arr)
    
    for r in range(n + 1):
        for comb in combinations(arr, r):
            sums.append(sum(comb))
            
    return sums


def meet_in_middle(arr, target):
    n = len(arr)

    # divide array
    left = arr[:n//2]
    right = arr[n//2:]

    # generate subset sums
    left_sums = subset_sums(left)
    right_sums = subset_sums(right)

    # convert to set for fast lookup
    right_set = set(right_sums)

    # check for exact sum
    for s in left_sums:
        if (target - s) in right_set:
            return True

    return False


# Test Case A
E1 = [1, 3, 9, 2, 7, 12]
target1 = 15

print("Array:", E1)
print("Exact Sum:", target1)
print("Subset Exists:", meet_in_middle(E1, target1))


print()

# Test Case B
E2 = [3, 34, 4, 12, 5, 2]
target2 = 15

print("Array:", E2)
print("Exact Sum:", target2)
print("Subset Exists:", meet_in_middle(E2, target2))
