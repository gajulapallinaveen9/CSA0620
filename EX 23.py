def strStr(haystack, needle):
    # Edge case: empty needle
    if not needle:
        return 0
    
    # Use Python's built-in find method
    return haystack.find(needle)


# Example usage:
print(strStr("sadbutsad", "sad"))   # Output: 0
print(strStr("leetcode", "leeto"))  # Output: -1
