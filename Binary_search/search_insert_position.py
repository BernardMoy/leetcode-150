class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Classic binary search. 
        Update the final value of l or l+1 
        based on whether target <= nums[l]
        """ 

        l, r = 0, len(nums)-1

        while l<r:
            m = (l+r)//2

            # left
            if target < nums[m]:
                r = m-1
            
            # right
            elif target > nums[m]:
                l = m+1
            
            # found
            else:
                return m
        
        # The final ans is either l or l+1
        if target<=nums[l]:
            return l
        else:
            return l+1
            