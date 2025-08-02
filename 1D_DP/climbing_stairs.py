class Solution:
    def climbStairs(self, n: int) -> int:
        """
        This is fibonacci sequence.
        """
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b

        return b
