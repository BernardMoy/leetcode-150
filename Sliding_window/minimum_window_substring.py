class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """ 
        Regular two pointer approach (for loop for r + while loop for l). 
        The d dictionary is to store the number of missing characters for the window
        whenever r moves, d[s[r]] always -= 1 and l moves, d[s[l]] always += 1 

        Main point is to use the length of t to determine if the window has all characters, instead of iterating the dict: 
        while shrinking, if d[s[l]] > 0 that means a required letter is being removed, length have to +1. 
        Because negative is allowed, > 0 means this
        """ 

        d = Counter(t) 
        remaining = len(t)
        l = 0 
        ans = "" 

        for r in range(len(s)): 
            if d[s[r]] > 0: 
                remaining -= 1 
            d[s[r]] -= 1 
            
            # shrink the left side while all remaining characters are found 
            while remaining == 0: 
                d[s[l]] += 1 

                if not ans or r-l+1 < len(ans): 
                    ans = s[l:r+1]

                # if d[s[l]] > 0 that means a required letter is being removed from the substring window
                # as the dictionary specifies the number of missing letters 
                if d[s[l]] > 0: 
                    remaining += 1 
                

                l += 1 
            
        return ans  
