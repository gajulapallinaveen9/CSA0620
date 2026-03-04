def minPatches(coins, target):
    coins.sort()
    miss = 1
    added = 0
    i = 0

    while miss <= target:
        if i < len(coins) and coins[i] <= miss:
            miss += coins[i]
            i += 1
        else:
            miss += miss
            added += 1

    return added


# Test
print(minPatches([1,4,10], 19))  # Output: 2
