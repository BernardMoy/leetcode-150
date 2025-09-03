class Solution:
    def trailingZeroes(self, n: int) -> int:
        """ 
        Trailing zeroes come from 2*5 (limiting is the number of 5s). 
        For larger numbers such as 25, there are two 5 factors (5*5) 
        the recursion count those as well 
        """ 
        
        if n == 0: 
            return 0 
        
        return n//5 + self.trailingZeroes(n//5)