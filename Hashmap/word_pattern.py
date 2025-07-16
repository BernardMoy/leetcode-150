class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Consider the case when different characters map to the same pattern. 
        """ 
        # Use a dict to store mappings 
        d ={}

        # Disallow two different characters map to the same pattern
        visited = set() 

        # Split s into list 
        s = s.split(' ')

        # Base case 
        if len(s) != len(pattern): 
            return False 

        for i in range(len(pattern)): 
            if pattern[i] in d and d[pattern[i]] != s[i]: 
                return False 
            
            if pattern[i] in d and d[pattern[i]] == s[i]: 
                continue 
            
            if s[i] in visited: 
                return False 

            d[pattern[i]] = s[i] 
            visited.add(s[i])
        
        return True 