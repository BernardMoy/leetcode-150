class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Scan the array and maintain a current sum: 
        update the current sum to keep track of the max (cmax) in each iteration.

        If current sum falls below 0 at any point, set it back to 0. 
        """
        # O(N) SCAN IT
        cmax = float('-inf')
        current = 0

        for n in nums:
            current += n
            
            # update the cmax value 
            if current > cmax:
                cmax = current

            # if the current sum is negative, make it 0
            if current < 0:
                current = 0

        
        return cmax