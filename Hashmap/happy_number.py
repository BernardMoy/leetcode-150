class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Notice the order of updating n, adding it to visited and checking n == 1
        """
        visited = set() 
        while True: 
            n = sum([int(x)*int(x) for x in str(n)])
            if n in visited: 
                return False 

            visited.add(n) 
            if n == 1: 
                return True 