class Solution:
    def totalNQueens(self, n: int) -> int:
        """ 
        Alternatively, this question is asking the number of placements where no two queens
        share the same row, column or diagonal 

        backtracking solution that checks places grid from a starting row, and find solutions starting at the next row
        As we havent placed the areas below the 'row' at that point we only have to check duplicates
        for vertical, top left and top right  (top area)
        """ 

        # helper function to find the number of combinations, placing from the row specified to n
        def helper(board, row): 
            # base case - a valid placement count as 1 
            if row == n: 
                return 1 
            
            count = 0 
            for col in range(n): 
                if canplace(board, row, col): 
                    # set the queen to be placed 
                    board[row][col] = 1 
                    
                    # recursive backtrack 
                    count += helper(board, row+1) 

                    # unset the position
                    board[row][col] = 0 
            
            return count 
        
        # check if a row and col position can be placed 
        def canplace(board, row, col): 
            # check if vertical have other queens (1) 
            for i in range(row): 
                if board[i][col]: 
                    return False 
            
            # check upper left diagonal 
            for i in range(1, 1+min(row, col)): 
                if board[row-i][col-i]: 
                    return False 

            # check upper right diagonal 
            for i in range(1, 1+min(row, n-col-1)): 
                if board[row-i][col+i]: 
                    return False 
            
            return True 

        
        board = [[0 for _ in range(n)] for _ in range(n)]

        # start row is 0
        return helper(board, 0)