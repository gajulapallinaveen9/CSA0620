def dice_throw(num_sides, num_dice, target):

    # create DP table
    dp = [[0 for _ in range(target + 1)] for _ in range(num_dice + 1)]

    # base case
    dp[0][0] = 1

    # fill DP table
    for i in range(1, num_dice + 1):
        for j in range(1, target + 1):
            for k in range(1, num_sides + 1):
                if j - k >= 0:
                    dp[i][j] += dp[i-1][j-k]

    return dp[num_dice][target]


# Test Case 1
sides1 = 6
dice1 = 2
target1 = 7

print("Test Case 1:")
print("Number of ways to reach sum 7:", dice_throw(sides1, dice1, target1))


# Test Case 2
sides2 = 4
dice2 = 3
target2 = 10

print("\nTest Case 2:")
print("Number of ways to reach sum 10:", dice_throw(sides2, dice2, target2))
