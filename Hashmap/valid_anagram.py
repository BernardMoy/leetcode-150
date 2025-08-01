class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Alternatively, subtract one counter from another
        """
        return Counter(s) == Counter(t)
