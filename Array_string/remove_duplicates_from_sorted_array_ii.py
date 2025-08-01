class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Duplicated elements must come together
        n == nums[i-2] means n == nums[i-1] == nums[n-2]
        """
        i = 0
        for n in nums:  # Cannot use pointer as nums is updated in place here
            if i < 2 or n != nums[i - 2]:
                nums[i] = n
                i += 1
        return i
