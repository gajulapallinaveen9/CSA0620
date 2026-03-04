def findPaths(m, n, N, i, j):
    from functools import lru_cache

    @lru_cache(None)
    def dp(steps, r, c):
        # If ball is out of bounds
        if r < 0 or r >= m or c < 0 or c >= n:
            return 1 if steps == 0 else 0

        # No moves left and still inside
        if steps == 0:
            return 0

        # Explore all 4 directions
        return (
            dp(steps - 1, r + 1, c) +
            dp(steps - 1, r - 1, c) +
            dp(steps - 1, r, c + 1) +
            dp(steps - 1, r, c - 1)
        )

    return dp(N, i, j)


# -------------------------
# Example Test Cases
# -------------------------
if __name__ == "__main__":
    print(findPaths(2, 2, 2, 0, 0))  # Output: 6
    print(findPaths(1, 3, 3, 0, 1))  # Output: 12
