class Solution:
    """ 
    Classic top down DP 
    that iterates over each word in word dict 
    and use sub-problem of a substring by trimming the front
    if s starts with that word in the word dict. 
    """ 
    def __init__(self): 
        self.d = {} 

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s in self.d: 
            return self.d[s] 

        if not s: 
            return True 
        
        ans = False 
        for word in wordDict: 
            if s.startswith(word) and self.wordBreak(s[len(word):], wordDict): 
                # words in word dict can be reused
                ans = True 
                break 
        
        self.d[s] = ans 
        return ans 