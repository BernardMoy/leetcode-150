class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = set(nums)

        for i, n in enumerate(nums):
            if (target - n) in s and nums.index((target - n)) != i:
                return [i, nums.index((target - n))]
