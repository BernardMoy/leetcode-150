class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Handling two portions: 
        based on the LEFTMOST value, determine if nums[m] is in the first or second portion
        if in the second portion, check if it is the first element of the second portion, 
        which is the min element. 
        """
        # base case: the list is not rotated 
        if nums[0] < nums[-1]: 
            return nums[0] 

        l, r = 0, len(nums)-1
        leftmost = nums[0]

        while l <= r: 
            m = (l+r)//2 
            if nums[m] > leftmost:   # the mid element is in the first portion
                l = m+1
            elif nums[m] < leftmost:   # it is in the second portion
                if m>0 and nums[m] < nums[m-1]:   # check if it is the first element in the second portion
                    return nums[m]
                r = m-1
            else: 
                break 
        
        # return this if not sure whether l or r contains the min 
        return min(nums[l], nums[r])