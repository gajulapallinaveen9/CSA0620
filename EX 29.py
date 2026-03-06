import itertools

# 1. Function to calculate total value of selected items
def total_value(items, values):
    return sum(values[i] for i in items)

# 2. Function to check feasibility of selected items
def is_feasible(items, weights, capacity):
    return sum(weights[i] for i in items) <= capacity

# 3. Exhaustive search for optimal selection
def knapsack(weights, values, capacity):
    n = len(weights)
    max_value = 0
    best_selection = []
    
    # Generate all subsets of items
    for r in range(n+1):
        for subset in itertools.combinations(range(n), r):
            if is_feasible(subset, weights, capacity):
                val = total_value(subset, values)
                if val > max_value:
                    max_value = val
                    best_selection = list(subset)
    
    return best_selection, max_value


# -------------------------------
# Test Cases
# -------------------------------

# Test Case 1
weights1 = [2, 3, 1]
values1 = [4, 5, 3]
capacity1 = 4
selection1, value1 = knapsack(weights1, values1, capacity1)
print("Test Case 1:")
print("Optimal Selection:", selection1)
print("Total Value:", value1)

# Test Case 2
weights2 = [1, 2, 3, 4]
values2 = [2, 4, 6, 3]
capacity2 = 6
selection2, value2 = knapsack(weights2, values2, capacity2)
print("\nTest Case 2:")
print("Optimal Selection:", selection2)
print("Total Value:", value2)
