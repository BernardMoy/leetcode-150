class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Divide and conquer: 
        Recursively call self.myPow(x, n//2)
        and multiply by x depending on whether n is ODD OR EVEN

        time complexity O(log(n))
        """ 

        # Handling negative n
        if n<0:
            return 1/self.myPow(x,-n)

        # Recursively call self.myPow(x, n//2)
        if n == 0:
            return 1
        elif n == 1:
            return x
        else:
            t = self.myPow(x, n//2)
            
            if n%2 == 1: # n is odd
                return t*t*x
            else:  # n is even
                return t*t