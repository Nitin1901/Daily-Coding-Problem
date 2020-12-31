def capacity(height):
    l = len(height)
    result = 0
    
    if l == 0:
        return result
    
    # Left max
    left = [0]*l
    left[0] = height[0]
    for i in range(1,l):
        left[i] = max(height[i], left[i-1])        
        
    # Right max
    right = [0]*l
    right[-1] = height[-1]
    for i in range(l-2, -1, -1):
        right[i] = max(height[i], right[i+1])        
    
    # Checking
    for i in range(l):
        result += min(left[i], right[i]) - height[i]
    
    return result

heights = list(map(int, input().split()))
print(capacity(heights))
        