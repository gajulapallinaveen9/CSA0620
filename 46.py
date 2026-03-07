def assembly_line(a1, a2, t1, t2, e1, e2, x1, x2, n):

    f1 = [0] * n
    f2 = [0] * n

    # Entry time
    f1[0] = e1 + a1[0]
    f2[0] = e2 + a2[0]

    # Compute minimum time for each station
    for i in range(1, n):
        f1[i] = min(f1[i-1] + a1[i], f2[i-1] + t2[i-1] + a1[i])
        f2[i] = min(f2[i-1] + a2[i], f1[i-1] + t1[i-1] + a2[i])

    # Exit time
    final_time = min(f1[n-1] + x1, f2[n-1] + x2)

    return final_time


# Example Input
n = 4

a1 = [4, 5, 3, 2]
a2 = [2, 10, 1, 4]

t1 = [7, 4, 5]
t2 = [9, 2, 8]

e1 = 10
e2 = 12

x1 = 18
x2 = 7

# Function call
result = assembly_line(a1, a2, t1, t2, e1, e2, x1, x2, n)

print("Minimum time required:", result)
