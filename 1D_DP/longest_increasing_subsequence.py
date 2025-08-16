class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Classic bottom up DP solution (not going into bisect)
        store the longest increasing subsequences from that point to the rightmost,
        in the longest array. 
        """
        # bottom up DP 
        longest = [1 for _ in range(len(nums))]

        for i in range(len(longest)-2, -1, -1): 
            for j in range(i+1, len(longest)): 
                if nums[i] < nums[j]: 
                    longest[i] = max(longest[i], longest[j] + 1)
        
        return max(longest)