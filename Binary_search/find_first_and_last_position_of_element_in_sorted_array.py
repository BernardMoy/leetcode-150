class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Binary search that requires you to find the leftmost and rightmost position of duplicated target. 

        Trick: 
        if nums[m] == target: 
            r = r-1 encourages it to find a "more left" solution
            and l = l+1 encourages it to find a "more right" solution. 
        
        then we can have the leftmost and rightmost position of an element. 
        """
        l = 0
        r = len(nums)-1

        index1, index2 = -1, -1

        # ============ Find left index ============
        while l<=r:
            m = (l+r)//2

            # cases
            if nums[m] < target:  # Search right
                l = m+1
            elif nums[m] > target:  # Search left
                r = m-1
            else:
                index1 = m
                # target found. return the leftmost index
                # Move right to the left until they overlaps
                r = r-1

        l = 0
        r = len(nums)-1

        # ============ Find right index ============
        while l<=r:
            m = (l+r)//2

            # cases
            if nums[m] < target:  # Search right
                l = m+1
            elif nums[m] > target:  # Search left
                r = m-1
            else:
                index2 = m
                # target found. return the leftmost index
                # Move right to the left until they overlaps
                l = l+1
        
        return [index1, index2]