class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """ 
        Use a while loop to keep track of the carry 
        """ 
        
        digits[-1] += 1 

        # increment all carry 
        i = len(digits) - 1
        while digits[i] == 10: 
            digits[i] = 0 
            i -= 1 
            
            if i < 0: 
                digits = [1] + digits 
            else: 
                digits[i] += 1 
        
        return digits 