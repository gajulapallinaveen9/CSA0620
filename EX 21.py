def findKthPositive(arr, k):
    missing_count = 0
    current = 1
    index = 0
    
    while True:
        if index < len(arr) and arr[index] == current:
            index += 1
        else:
           
            missing_count += 1
            if missing_count == k:
                return current
        current += 1

print(findKthPositive([2,3,4,7,11], 5))  
print(findKthPositive([1,2,3,4], 2))     
