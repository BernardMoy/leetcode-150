class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Method 1: Sort, then index 
        Method 2: Add to a max heap, then pop k times
        Method 3: Quick select algorithm
        """ 
        t = [-x for x in nums]
        heapq.heapify(t)
        for i in range(k-1):
            heapq.heappop(t)
        
        return -heapq.heappop(t)