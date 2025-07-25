class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Use a counter that decreases the count when iterating.
        """
        
        c = Counter(magazine) 
        
        for letter in ransomNote: 
            if letter not in c: 
                return False
            elif c[letter] == 0:
                return False
            else: 
                c[letter] -= 1 
        
        return True 