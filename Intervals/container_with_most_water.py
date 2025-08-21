class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Greedy + 2 pointer solution.
        Maintain a left and right pointer, and shrink the side when that side has a smaller height
        in an attempt to maximize the volume when its height is taller.
        """

        l, r = 0, len(height) - 1
        cur = (r - l) * min(height[l], height[r])  # volume depends on the lower height

        while l <= r:
            # Move the pillar with a lower height
            if height[l] < height[r]:
                l += 1
                cur = max(cur, (r - l) * min(height[l], height[r]))

            else:
                r -= 1
                cur = max(cur, (r - l) * min(height[l], height[r]))

        return cur
