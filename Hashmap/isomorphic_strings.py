class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Use a visited set to ensure that "No two characters may map to the same character".
        """
        d = {}
        visited = set()

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in d:
                if t[i] in visited:
                    return False
                d[s[i]] = t[i]
                visited.add(t[i])

            elif d[s[i]] != t[i]:
                return False

        return True
