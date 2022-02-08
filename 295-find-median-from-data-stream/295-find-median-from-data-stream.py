from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.heap_bigger = []     #stores the values bigger than the median (min is the root)
        self.heap_smaller = []    #stores the values smaller than the median (-max is the root)
        

    def addNum(self, num: int) -> None:
        #if empty we arbitrarly push num into heap_bigger
        if len(self.heap_bigger) + len(self.heap_smaller) == 0:
            heappush(self.heap_bigger, num)
            return
            
        #Push num depending on whether it is bigger than median or not
        if num < self.findMedian():
            heappush(self.heap_smaller, -num)
        else:
            heappush(self.heap_bigger, num) 
            
        #Keep the heaps with difference in size of at least one
        if len(self.heap_smaller) > len(self.heap_bigger) + 1:
            root = - heappop(self.heap_smaller)
            heappush(self.heap_bigger, root)
        elif len(self.heap_bigger) > len(self.heap_smaller) + 1:
            root =  heappop(self.heap_bigger)
            heappush(self.heap_smaller, -root)
            
        

    def findMedian(self) -> float:
        if len(self.heap_bigger) == len(self.heap_smaller):
            return (self.heap_bigger[0] -self.heap_smaller[0])/2
        elif len(self.heap_bigger) > len(self.heap_smaller):
            return self.heap_bigger[0]
        else:
            return -self.heap_smaller[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()