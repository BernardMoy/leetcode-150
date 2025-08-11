class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        backtrack function that takes in a start index.
        For every index from the start to the end of the list,
        try swapping the elements, backtrack, and then swap them back.
        """
        ans = []

        def backtrack(start):
            if start == len(nums):
                ans.append(nums[:])

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return ans
