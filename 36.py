# Binary Search with step-by-step trace and comparison counter

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        print(f"Checking mid index {mid} (value {arr[mid]})")

        if arr[mid] == key:
            print(f"Element {key} found at index {mid} (1-based position {mid+1})")
            return mid + 1, comparisons  # return 1-based position
        elif arr[mid] < key:
            print(f"{arr[mid]} < {key}, move right")
            low = mid + 1
        else:
            print(f"{arr[mid]} > {key}, move left")
            high = mid - 1

    print(f"Element {key} not found")
    return -1, comparisons


# Test Case 1
arr1 = [3,9,14,19,25,31,42,47,53]
key1 = 31
print("Input:", arr1, "Search Key:", key1)
pos, comps = binary_search(arr1, key1)
print("Output: Position =", pos, "Comparisons =", comps)

# Test Case 2
arr2 = [13,19,24,29,35,41,42]
key2 = 42
print("\nInput:", arr2, "Search Key:", key2)
pos, comps = binary_search(arr2, key2)
print("Output: Position =", pos, "Comparisons =", comps)

# Test Case 3
arr3 = [20,40,60,80,100,120]
key3 = 60
print("\nInput:", arr3, "Search Key:", key3)
pos, comps = binary_search(arr3, key3)
print("Output: Position =", pos, "Comparisons =", comps)
