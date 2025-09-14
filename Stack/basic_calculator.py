class Solution:
    def calculate(self, s: str) -> int:
        """ 
        Use cur to store the current number, and sign for + or - (added to total ans when seen a new one) 
        
        The stack here is used for keeping track of previous ans and sign, 
        so that when ( is encountered, ans and sign can be reset to their default value
        and added back to total and when ) is encountered by popping from the stack. 
        """ 

        cur = 0  # current (unsigned) number 
        ans = 0  # total number 
        sign = 1 # 1 or -1 
        stack = [] 

        for char in s: 
            if char.isdigit(): 
                # append the char to the right of cur 
                cur = cur * 10 + int(char) 
            
            elif char == '+' or char == '-': 
                # when encountered + or -, add the cur number to ans
                ans += sign*cur 

                # update sign for the next number 
                sign = 1 if char == '+' else -1 
                
                # reset cur to look for the next number 
                cur = 0 
            
            elif char == '(': 
                # use the stack to store the previous ans and sign 
                stack.append(ans) 
                stack.append(sign) 
                
                # reset the ans and sign to their defaults to be used in the scope of paranthesis 
                ans = 0 
                sign = 1

            elif char == ')':
                ans += sign*cur 

                # add the previous result from the stack back to ans 
                old_sign = stack.pop() 
                old_ans = stack.pop() 
                ans = ans*old_sign + old_ans   # 1-(-2) -> [ans = -2, old_ans = 1, old_sign = -1]
                cur = 0 
        
        # add the last cur value 
        ans += sign*cur 
        return ans 
