from collections import deque

def max_sliding_window(arr, k):
    n = len(arr)
    if n == 0:
        return []
    if k == 1:
        return arr 

    dq = deque()
    result = []

    for i in range(n):
        
        while dq and dq[0] <= i - k:
            dq.popleft()

     
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()

        dq.append(i)

        
        if i >= k - 1:
            result.append(arr[dq[0]])

    return result




print(max_sliding_window([1, 5, 3, 2, 4, 6], 3))          
print(max_sliding_window([1, 2, 3, 4], 2))                
print(max_sliding_window([7, 7, 7, 7], 1))               
                       
