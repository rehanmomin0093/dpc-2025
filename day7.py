def trap(height):
    n = len(height)
    if n < 3:
        return 0  # Less than 3 bars -> no water can be trapped
    
    left, right = 0, n - 1
    leftMax, rightMax = 0, 0
    trapped = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= leftMax:
                leftMax = height[left]
            else:
                trapped += leftMax - height[left]
            left += 1
        else:
            if height[right] >= rightMax:
                rightMax = height[right]
            else:
                trapped += rightMax - height[right]
            right -= 1
    
    return trapped
n = int(input("Enter number of bars: "))
height = list(map(int, input("Enter bar heights separated by space: ").split()))

if len(height) != n:
    print("Error: Number of heights entered doesn't match n.")
else:
    print("Total water trapped:", trap(height))
