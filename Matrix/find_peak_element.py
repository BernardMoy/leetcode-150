class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Our target is to find an index m such that nums[m] > nums[m-1] and nums[m] > nums[m+1]
        
        If nums[m] > nums[m-1], it is on the right side of a downward opening parabola
        Hence search left to find the peak point of that parabola. 
        Same for the opposite (nums[m] > nums[m+1]). 
        """
        l, r = 0, len(nums)-1

        while l<=r: 
            m = (l+r)//2 
            if m>0 and nums[m] < nums[m-1]: 
                r = m-1   # Search left 
            elif m<len(nums)-1 and nums[m] < nums[m+1]: 
                l = m+1   # Sesrch right 
            else: 
                return m 
        
        return -1