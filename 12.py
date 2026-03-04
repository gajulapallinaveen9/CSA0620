def rob(nums):
    # If only one house
    if len(nums) == 1:
        return nums[0]

    # Helper function for normal House Robber (linear)
    def rob_linear(arr):
        prev1 = 0  # max till previous house
        prev2 = 0  # max till house before previous
        
        for money in arr:
            temp = prev1
            prev1 = max(prev2 + money, prev1)
            prev2 = temp
        
        return prev1

    # Case 1: Exclude last house
    case1 = rob_linear(nums[:-1])

    # Case 2: Exclude first house
    case2 = rob_linear(nums[1:])

    return max(case1, case2)


# -------------------------
# Example Test Cases
# -------------------------
if __name__ == "__main__":
    print(rob([2, 3, 2]))      # Output: 3
    print(rob([1, 2, 3, 1]))   # Output: 4
