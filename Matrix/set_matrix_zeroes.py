class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Achieve O(1) space by using a placeholder
        to indicate values that are set to 0 but not initially 0. 
        """
        for r in range(len(matrix)): 
            for c in range(len(matrix[0])): 
                if matrix[r][c] == 0: 

                    # set all its row and col elements to 'a' (placeholder) 
                    for ii in range(len(matrix[0])): 
                        if matrix[r][ii] != 0:
                            matrix[r][ii] = 'a'

                    for jj in range(len(matrix)): 
                        if matrix[jj][c] != 0: 
                            matrix[jj][c] = 'a'
        
        # Change all 'a' to 0 in the matrix 
        for r in range(len(matrix)): 
            for c in range(len(matrix[0])): 
                if matrix[r][c] == 'a': 
                    matrix[r][c] = 0

        return matrix 
        