class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Binary search.
        It requires the rounded down integer,
        so return the previous integer if l*l > x
        """

        l = 0
        h = 2**31 - 1

        while l < h:
            m = (l + h) // 2

            if m * m > x:
                # search the left side
                h = m - 1

            else:
                # search the right side
                l = m + 1

        if l * l > x:
            return l - 1
        return l
