class Solution:
    def isValid(self, s: str) -> bool:
        stx = [] 
        for c in s: 
            if not stx or c in ['(', '[', '{']: 
                stx.append(c) 
                continue 
            
            if c == ')' and stx[-1] == '(': 
                stx.pop() 
                continue 
            
            if c == ']' and stx[-1] == '[': 
                stx.pop() 
                continue 
            
            if c == '}' and stx[-1] == '{':
                stx.pop()
                continue 
            
            return False 

        return len(stx) == 0