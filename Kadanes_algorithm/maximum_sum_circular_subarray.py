class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """ 
        Refer "maximum subarray" problem 
        find the maximum AND minimum subarray using the same (flipped) logic 

        if max subarray (cmax > 0), then the ans can be in the middle or wraps around the array
        Wrap around solution is found by --> SUM(ARR) - MINIMUM SUBARRAY <-- (main point). 
        """
        cmax = float('-inf')
        current = 0
        cmin = float('inf') 
        current2 = 0 

        for n in nums:
            current += n
            current2 += n 
            
            # update the cmax and cmin values
            if current > cmax:
                cmax = current
            if current2 < cmin: 
                cmin = current2 

            # if the current sum is negative, make it 0
            if current < 0:
                current = 0
            if current2 > 0: 
                current2 = 0 

        if cmax > 0: 
            return max(cmax, sum(nums) - cmin)
        else: 
            return cmax