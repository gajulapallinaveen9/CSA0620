import itertools

# 1. Function to calculate total cost of an assignment
def total_cost(assignment, cost_matrix):
    return sum(cost_matrix[i][assignment[i]] for i in range(len(assignment)))

# 2. Exhaustive search for optimal assignment
def assignment_problem(cost_matrix):
    n = len(cost_matrix)
    workers = list(range(n))
    tasks = list(range(n))
    
    min_cost = float('inf')
    best_assignment = None
    
    # Generate all permutations of tasks
    for perm in itertools.permutations(tasks):
        cost = total_cost(perm, cost_matrix)
        if cost < min_cost:
            min_cost = cost
            best_assignment = perm
    
    # Format result as (worker, task) pairs
    assignment_pairs = [(f"worker {i+1}", f"task {best_assignment[i]+1}") for i in range(n)]
    return min_cost, assignment_pairs


# -------------------------------
# Test Cases
# -------------------------------

# Test Case 1
cost_matrix1 = [
    [3, 10, 7],
    [8, 5, 12],
    [4, 6, 9]
]
min_cost1, assignment1 = assignment_problem(cost_matrix1)
print("Test Case 1:")
print("Optimal Assignment:", assignment1)
print("Total Cost:", min_cost1)

# Test Case 2
cost_matrix2 = [
    [15, 9, 4],
    [8, 7, 18],
    [6, 12, 11]
]
min_cost2, assignment2 = assignment_problem(cost_matrix2)
print("\nTest Case 2:")
print("Optimal Assignment:", assignment2)
print("Total Cost:", min_cost2)
