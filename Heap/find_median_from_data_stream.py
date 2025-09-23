class MedianFinder:
    """ 
    Maintain a sorted array that maintains its sorted order when elements are added
    Done using bisect_left to insert at a specific position at log n time 
    and the median can be retrieved in O(1) time by inspecting the length of the array stored. 
    """ 
    
    def __init__(self):
        self.arr = [] 

    def addNum(self, num: int) -> None:
        if not self.arr: 
            self.arr.append(num) 
        else: 
            pos = bisect.bisect_left(self.arr, num) 
            self.arr.insert(pos, num) 
        

    def findMedian(self) -> float:
        N = len(self.arr)
        if N % 2 == 0: 
            return (self.arr[N//2-1] + self.arr[N//2])/2.0
        
        else: 
            return self.arr[N//2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()