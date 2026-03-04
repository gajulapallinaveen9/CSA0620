import math

def uniquePaths(m, n):
    # Total moves needed
    total_moves = m + n - 2
    
    # Choose (m-1) downs (or choose (n-1) rights)
    return math.comb(total_moves, m - 1)


# -------------------------
# Example Test Cases
# -------------------------
if __name__ == "__main__":
    print(uniquePaths(7, 3))  # Output: 28
    print(uniquePaths(3, 2))  # Output: 3
    
