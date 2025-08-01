class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Use the startswith function.
        """

        for i in range(len(haystack)):
            if haystack[i::].startswith(needle):
                return i

        return -1
