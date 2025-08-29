class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Use an array of arrays to do simulation
        while index < len(s), 
        append vertically downwards, then append diagonally upwards. 
        """
        # base case: vertical string 
        if numRows >= len(s): 
            return s 
        
        arr = [[] for _ in range(numRows)]
        i = 0 
        while i < len(s): 
            # Append words vertically 
            for j in range(numRows): 
                arr[j].append(s[i]) 
                i += 1 
                if i >= len(s): 
                    break 

            if i >= len(s): 
                break 
            # Append words horizontally 
            for j in range(numRows-2, 0, -1): 
                arr[j].append(s[i])
                i += 1 
                if i >= len(s): 
                    break 
        
        # Merge the arrays into strings 
        s = ''.join([''.join(x) for x in arr])
        return s
