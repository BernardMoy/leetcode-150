class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        bottom up DP is used (as it involves caching the entire subarray of nums)
        you only need to cache two values to build the solution to the front. 
        """ 

        # base case 
        if len(nums) < 2: 
            return max(nums)

        # remember at this point, the second last element can choose either nums[-2] or nums[-1]
        a, b = max(nums[-2], nums[-1]), nums[-1]

        for i in range(len(nums)-3, -1, -1): 
            a, b = max(nums[i] + b, a), a
        
        return max(a,b)