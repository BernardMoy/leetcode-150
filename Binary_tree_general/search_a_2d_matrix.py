class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Binary search the row first, then column within that row 
        consider the largest (Rightmost) element and the smallest (Leftmost) element of the row. 

        m is the index of the row after breaking (as target has to be within matrix[m] when breaking)
        """ 

        ROWS, COLS = len(matrix), len(matrix[0])

        # Binary search the row 
        t, b = 0, ROWS-1
        while t <= b: 
            m = (t+b)//2 
            # Larger than m's largest -> search right 
            if target > matrix[m][-1]: 
                t = m+1

            # Smaller than m's smallest -> search left 
            elif target < matrix[m][0]: 
                b = m-1
            
            else: break 
        
        # Base case: Target not found to belong to any row
        if (t > b): 
            return False 

        # m is the index of the row after breaking
        # Binary search the column within that row 
        l, r = 0, COLS-1
        row = (t+b)//2
        while l<=r: 
            m = (l+r)//2 
            if target > matrix[row][m]: 
                l = m+1
            elif target < matrix[row][m]: 
                r = m-1
            else: 
                return True 
        
        return False 