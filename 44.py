# Karatsuba Multiplication

def karatsuba(x, y):

    # Base case
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Split numbers
    high1 = x // 10**m
    low1 = x % 10**m
    high2 = y // 10**m
    low2 = y % 10**m

    # 3 recursive multiplications
    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)

    # Karatsuba formula
    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0


# Test Case
x = 1234
y = 5678

z = karatsuba(x, y)

print("x =", x)
print("y =", y)
print("Product (Karatsuba) =", z)
