class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Handling two base cases.
        """
        # if s is a subseq of t, len(s) <= len(t)
        if len(s) > len(t):
            return False

        # Base case: if s is empty, it is always subsequence of t
        if len(s) == 0:
            return True

        i = 0
        for j in range(len(t)):
            if s[i] == t[j]:
                i += 1

                # Early break
                if i == len(s):
                    return True

        # The entire length of s should have been traversed
        return i == len(s)
