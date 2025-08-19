def findLeaders(arr):
    n = len(arr)
    leaders = []
    max_from_right = float('-inf')
    
    for i in range(n-1, -1, -1):
        if arr[i] >= max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]
    
    leaders.reverse()
    return leaders


n = int(input("Enter size of array: "))
arr = []

for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    arr.append(val)

result = findLeaders(arr)
print("Leaders:", result)
