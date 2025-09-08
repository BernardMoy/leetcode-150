class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """ 
        Main idea: N = N & (N-1) unsets the rightmost set bit in N 
        if right > left and that bit can be unset, that bit will be 0 after AND because it is not common to all numbers
        """ 
        
        while right>left:
            right &=(right-1)
        return right