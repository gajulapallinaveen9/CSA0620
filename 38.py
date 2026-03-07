# Count tuples where A[i] + B[j] + C[k] + D[l] == 0

def fourSumCount(A, B, C, D):
    from collections import Counter
    
    # Step 1: Compute all possible sums of A[i] + B[j]
    AB_sum = Counter(a + b for a in A for b in B)
    
    count = 0
    
    # Step 2: For each possible sum of C[k] + D[l], check if -(C+D) exists in AB_sum
    for c in C:
        for d in D:
            target = -(c + d)
            if target in AB_sum:
                count += AB_sum[target]
    
    return count


# Test Case 1
A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]
print("Input:", A, B, C, D)
print("Output:", fourSumCount(A, B, C, D))  # Expected 2

# Test Case 2
A = [0]
B = [0]
C = [0]
D = [0]
print("\nInput:", A, B, C, D)
print("Output:", fourSumCount(A, B, C, D))  # Expected 1
