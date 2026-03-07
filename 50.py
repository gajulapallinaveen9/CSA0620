def longestPalindrome(s):

    res = ""
    
    for i in range(len(s)):
        
        # Odd length palindrome
        l = r = i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len(res):
                res = s[l:r+1]
            l -= 1
            r += 1
        
        # Even length palindrome
        l, r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len(res):
                res = s[l:r+1]
            l -= 1
            r += 1

    return res


# Test Cases
s1 = "babad"
print("Input:", s1)
print("Output:", longestPalindrome(s1))

s2 = "cbbd"
print("\nInput:", s2)
print("Output:", longestPalindrome(s2))
