class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Moving l to the right increases the result, and moving r to the left decreases it. 
        Squeeze the ans.  
        """ 

        l = 0 
        r = len(numbers) -1 

        while numbers[l] + numbers[r] != target: 
            # if too large, move r to the left 
            if numbers[l] + numbers[r] > target: 
                r -= 1 

            # if too small, move l to the right 
            else: 
                l += 1

        # Solution is 1-indexed
        return [l+1, r+1]