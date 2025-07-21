class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        use a while loop to shrink the left part
        for sliding window problems.
        """ 

        visited = set() 
        l = 0 
        ans = 0 

        for r, c in enumerate(s): 
            # Shrink left while there are duplicates 
            while c in visited: 
                visited.remove(s[l])  # s[l] is the removed character 
                l += 1 

            visited.add(c) 
            ans = max(ans, r-l+1) 
        
        return ans 