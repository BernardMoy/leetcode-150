class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Sort array first, then use two pointer approach to handle l, r pointers
        to the right of the point of iteration (i). 
        Refer two sum II 
        """
        nums.sort() 
        ans = [] 

        for i in range(len(nums)): 
            if i>0 and nums[i] == nums[i-1]: 
                continue 
            
            l, r = i+1, len(nums)-1 
            while l < r: 
                total = nums[i] + nums[l] + nums[r]

                # if too large, decrement right pointer 
                if total > 0: 
                    r -= 1 
                # if too small, increment left pointer 
                elif total < 0: 
                    l += 1 
                else: 
                    ans.append([nums[i], nums[l], nums[r]])
                    # Shrink left and right pointers to the point that they have different vlues than before, so no duplicates are contained 
                    l += 1 
                    r -= 1 
                    while l < r and nums[l] == nums[l-1]: 
                        l += 1 
                    while l < r and nums[r] == nums[r+1]: 
                        r -= 1 
        return ans 