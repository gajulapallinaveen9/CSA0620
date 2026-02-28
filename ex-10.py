def heapify(nums, n, i):
    # Assume i is the largest, then check children
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and nums[left] > nums[largest]:
        largest = left
    if right < n and nums[right] > nums[largest]:
        largest = right

    # If largest is not root, swap and keep fixing
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heapify(nums, n, largest)


def heap_sort(nums):
    n = len(nums)

    # Step 1: Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i)

    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]  # swap
        heapify(nums, i, 0)

    return nums


# Example
nums = [4, 10, 3, 5, 1]
print(heap_sort(nums))  # Output: [1, 3, 4, 5, 10]
