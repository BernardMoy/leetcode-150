class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Use // to extract the most significant digit
        and %10 to extract the least significant digit.
        Without converting the number to a string.
        """

        # Base cases
        if x < 0:
            return False
        if x < 10:
            return True

        # Get the most significant digit
        num = 1
        while x >= 10 * num:
            num *= 10

        # While loop
        while x:
            rightmost = x % 10
            leftmost = x // num

            if rightmost != leftmost:
                return False

            # remove the rightmost and leftmost digit from x
            x = (x % num) // 10

            # We have removed 2 digits, so shrink num by 2 times
            num = num / 100

        return True
