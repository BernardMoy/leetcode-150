class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Use a while loop to shrink the left pointer.
        """

        visited = set()
        l = 0

        for r in range(len(nums)):
            # Shrink the window by incrementing left ptr
            while r - l > k:
                visited.remove(nums[l])
                l += 1

            if nums[r] in visited:
                return True

            visited.add(nums[r])

        return False
