class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        O(n) solution: Use a right pointer to iterate every position
        shrink the left pointer while current sum >= target
        and update the answer in the progress 
        """
        l = 0
        cursum = 0 
        ans = len(nums) + 1
        
        for r in range(len(nums)): 
            cursum += nums[r] 
            while cursum >= target: 
                ans = min(ans, r-l+1)
                cursum -= nums[l] 
                l += 1 
            
        
        return ans if ans < len(nums) + 1 else 0 