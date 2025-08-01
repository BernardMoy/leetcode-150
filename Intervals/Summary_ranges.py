class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """ 
        Use a while loop to skip all elements that are in order, i.e. consecutive. 
        """ 
        ans = [] 
        i = -1

        while i < len(nums)-1: 
            i += 1 

            # Keep track of the first element 
            first = nums[i] 

            # Skip all elements that are correct in order 
            while i < len(nums)-1 and nums[i] + 1 == nums[i+1]: 
                i += 1 

            if nums[i] != first: 
                ans.append(f"{first}->{nums[i]}")
            else: 
                ans.append(f"{nums[i]}")


        return ans 