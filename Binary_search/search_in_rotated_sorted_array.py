class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        Use whether nums[m] >= nums[l] (The leftmost element) 
        to determine the direction of search. 
        if nums[m] >= nums[l], target > nums[m] or target < nums[l]
        indicates the target must be right of m. 
        """
        l = 0
        r = len(nums) - 1

        m = -1


        # Binary search
        while l<=r:
            m = (l+r)//2

            if nums[m] == target:
                return m

            if nums[m] >= nums[l]: # Must be in the LEFT portion
                if target > nums[m] or target < nums[l]:  # Search right
                    l  = m+1
                else:
                    r  = m-1


            else:  # Must be in the RIGHT Portion
                if target < nums[m] or target > nums[r]:  # Search left
                    r = m-1
                else:
                    l = m+1
    
        return -1
            