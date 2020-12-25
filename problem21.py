import heapq as heap

def minClasses(arr):
    if arr == []:
        return 0
    arr.sort()
    h = []
    classes = 0
    for i in arr:
        while h and h[0] <= i[0]:
            heap.heappop(h)
        heap.heappush(h, i[1])
        classes = max(len(h), classes)
    return classes

arr = [(30,75),(0,50),(60,150),(80,120)]
print(minClasses(arr))