def palindrome(s):
    return s == s[::-1]
a = ["ran", "racecar", "game", "tenet"]
n = next((i for i in a if palindrome(i)), None)
print(n)
