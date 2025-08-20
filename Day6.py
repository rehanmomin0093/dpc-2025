def find_zero_sum_subarrays(arr):
    prefix_sum = 0
    hashmap = {}  
    result = []

    for i, num in enumerate(arr):
        prefix_sum += num

    
        if prefix_sum == 0:
            result.append((0, i))

        
        if prefix_sum in hashmap:
            for start_index in hashmap[prefix_sum]:
                result.append((start_index + 1, i))

        
        hashmap.setdefault(prefix_sum, []).append(i)

    return result

n = int(input("Enter number of elements in array: "))
arr = []
print("Enter the elements one by one:")
for _ in range(n):
    arr.append(int(input()))

result = find_zero_sum_subarrays(arr)

print("\nZero-sum subarrays (start_index, end_index):")
print(result if result else "No subarray with sum 0 found.")
