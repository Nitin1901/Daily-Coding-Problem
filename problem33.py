class MedianFinder:

    def __init__(self):
        self.array = []
        self.l = 0

    def addNum(self, num: int) -> None:
        if self.array == []:
            self.array = [num]
        else:
            right_place = 0
            while self.array[right_place] <= num:
                right_place += 1
                if right_place == self.l:
                    break
            self.array.insert(right_place, num)
        self.l += 1 

    def findMedian(self) -> float:
        if self.l%2 == 0:
            result = (self.array[int(self.l/2)-1]+self.array[int(self.l/2)])/2
        else:
            result = (self.array[self.l//2])
        if int(result) == result:
            return int(result)
        return result

x = list(map(int, input().split()))
obj = MedianFinder()
for e in x:
    obj.addNum(e)
    print(obj.findMedian())