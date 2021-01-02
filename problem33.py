import heapq

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right):
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)
        self.rebalance()

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return (-self.left[0]+self.right[0])/2

    def rebalance(self):
        l = -self.left[0]
        r = self.right[0] if self.right else float('inf')
        if l > r:
            l = -heapq.heappop(self.left)
            r = heapq.heappop(self.right)
            heapq.heappush(self.left, -r)
            heapq.heappush(self.right, l)

x = list(map(int, input().split()))
obj = MedianFinder()
for e in x:
    obj.addNum(e)
    print(obj.findMedian())