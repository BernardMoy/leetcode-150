class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # use the startswith function
        for i in range(len(haystack)): 
            if haystack[i::].startswith(needle): 
                return i 
        
        return -1 