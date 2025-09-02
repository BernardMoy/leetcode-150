class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Use a stack to store the numbers, pop two of them at a time. 
        Note that b//a does not work for divisions (it needs to truncate the decimal part)
        """
        stx = [] 
        for t in tokens: 
            if t not in ["+", "-", "*", "/"]: 
                stx.append(int(t)) 

            elif t == "+": 
                a = stx.pop() 
                b = stx.pop() 
                stx.append(a+b) 
            
            elif t == "-": 
                a = stx.pop() 
                b = stx.pop() 
                stx.append(b-a) 
            
            elif t == "*": 
                a = stx.pop() 
                b = stx.pop() 
                stx.append(a*b) 
            
            elif t == "/": 
                a = stx.pop() 
                b = stx.pop() 
                stx.append(int(b/a)) 
            
        return stx[0]