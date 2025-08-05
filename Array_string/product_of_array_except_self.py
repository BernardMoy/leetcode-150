class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Avoid using the division operation by pre-computing
        the POSTFIX and PREFIX multiplication array.

        For O(1) space complexity, store the prefix and postfix operations
        in the answer array instead. 
        """ 

        prefix, postfix = nums.copy(), nums.copy()
        for i in range(1, len(nums)): 
            prefix[i] *= prefix[i-1]
        for i in range(len(nums)-2, -1, -1): 
            postfix[i] *= postfix[i+1] 
        
        # Modify the nums array to get ans 
        for i in range(len(nums)): 
            # first and last element 
            if i == 0: 
                nums[i] = postfix[i+1]
            elif i == len(nums)-1:
                nums[i] = prefix[i-1]
            else: 
                nums[i] = postfix[i+1] * prefix[i-1]
        
        return nums 