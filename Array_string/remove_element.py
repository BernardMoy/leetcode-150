class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        j is the pointer that is assigned value only when nums != val
        i is only advanced when the current position value is not val
        """

        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i
