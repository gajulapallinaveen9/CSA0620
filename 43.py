# Strassen Matrix Multiplication for 2x2 matrix

def strassen(A, B):

    a, b = A[0][0], A[0][1]
    c, d = A[1][0], A[1][1]

    e, f = B[0][0], B[0][1]
    g, h = B[1][0], B[1][1]

    # Strassen formulas
    M1 = (a + d) * (e + h)
    M2 = (c + d) * e
    M3 = a * (f - h)
    M4 = d * (g - e)
    M5 = (a + b) * h
    M6 = (c - a) * (e + f)
    M7 = (b - d) * (g + h)

    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    C = [[C11, C12],
         [C21, C22]]

    return C


# Test Case
A = [[1,7],
     [3,5]]

B = [[6,8],
     [4,2]]

C = strassen(A,B)

print("Matrix A:")
for i in A:
    print(i)

print("\nMatrix B:")
for i in B:
    print(i)

print("\nProduct Matrix C:")
for i in C:
    print(i)
