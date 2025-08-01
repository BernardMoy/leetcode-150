class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        First strip the end,
        then return the value when a space is found or the entire string is traversed
        """

        s = s.strip()
        ans = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                return ans
            else:
                ans += 1

        return ans
