class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # j is the pointer that always advances
        i = 0
        for j in range(len(nums)):
            if (
                j == 0 or nums[j] != nums[j - 1]
            ):  # Duplicatd elements must come together
                nums[i] = nums[j]
                i += 1
        return i
