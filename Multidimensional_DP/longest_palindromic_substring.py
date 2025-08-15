class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Expand from a center point (i) for both the odd case and even case.
        For the even case, note the following:
        1. first check if the center two point is equal.
        2. it has to iterate one less time than the odd case (last iteration will be out of bounds)
        """

        # base case
        if not s:
            return ""
        if len(s) == 1:
            return s

        ansL = -1
        ansR = -1
        ansLength = 0

        for i in range(len(s)):
            # Consider expanding an odd length palindrome, where i is the central element.
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > ansLength:
                    ansL = l
                    ansR = r
                    ansLength = r - l + 1

                l -= 1
                r += 1

            # Consider expanding an even length palindrome, where i is the left element of the two central elements.
            l, r = i, i + 1
            if r < len(s) and s[r] == s[l]:
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if (r - l + 1) > ansLength:
                        ansL = l
                        ansR = r
                        ansLength = r - l + 1

                    l -= 1
                    r += 1

        return s[ansL : ansR + 1]
