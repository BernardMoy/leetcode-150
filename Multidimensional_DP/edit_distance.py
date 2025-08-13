class Solution:
    def __init__(self): 
        self.d = {} 

    def minDistance(self, word1: str, word2: str) -> int:
        """ 
        Top down DP
        
        Main point is handling swapping of characters: 
        if word1 and word2 starts with the same character, 
        no need to add 1 to the sub-problem, otherwise need. 
        """ 
        if (word1, word2) in self.d: 
            return self.d[(word1, word2)]

        # base cases 
        if word1 == word2: 
            return 0 
        if not word1: 
            return len(word2)  # All are insertions 
        if not word2: 
            return len(word1) 
        
        ans = 0 
        # if word1 and word2 starts with the same character, it is always preferable to skip it 
        if word1[0] == word2[0]: 
            ans = self.minDistance(word1[1::], word2[1::])

        # Simulate the 3 operations
        else: 
            a = self.minDistance(word1[1::], word2) 
            b = self.minDistance(word1, word2[1::])
            c = self.minDistance(word1[1::], word2[1::])

            ans = 1+min(a,b,c)
        
        self.d[(word1, word2)] = ans 
        return ans 