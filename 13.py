def climbStairs(n):
    if n <= 2:
        return n
    prev1 = 2 
    prev2 = 1 
    for _ in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    return prev1
if __name__ == "__main__":
    print(climbStairs(4))
    print(climbStairs(3))
