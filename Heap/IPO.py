class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        """ 
        The challenge is to heappop the max profit while keeping the capital <= current value 

        Use two heaps, one min heap for not yet available capitals and profits (does not meet capital <= current value) 
        another max heap for already available profits
        During each iteration, transfer the not yet available ones to the available heap
        and pop the profit from the available heap. 
        """ 

        notyetavailable = list(zip(capital, profits))   # (capital, profit) min heap
        available = []   # profit max heap 
        heapq.heapify(notyetavailable) 
        heapq.heapify(available)

        ans = w   # w is the initial value 
        for _ in range(k): 
            # add all profits from not yet available to available by popping 
            while notyetavailable and notyetavailable[0][0] <= ans: 
                c, p = heapq.heappop(notyetavailable) 
                heapq.heappush(available, -p) 
            
            # pop the max profit from available and add to ans 
            if available: 
                ans += -heapq.heappop(available)
        
        return ans