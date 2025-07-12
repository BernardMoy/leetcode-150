class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for n in nums:  # Cannot use pointer as nums is updated in place here
            if i < 2 or n != nums[i - 2]:  # Duplicatd elements must come together
                nums[i] = n
                i += 1
        return i
