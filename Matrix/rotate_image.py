class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Brute force: Check duplicate for every row, col and square. 
        """ 
        
        def check_duplicate(l): 
            visited = set() 
            for c in l: 
                if c != '.' and c in visited: 
                    return False 
                else: 
                    visited.add(c) 
            return True 

        for row in board: 
            if not check_duplicate(row): 
                return False 
        
        for i in range(len(board)): 
            col = [row[i] for row in board]
            if not check_duplicate(col): 
                return False 
        
        for r,c in [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]: 
            sq = [board[r][c], board[r][c+1], board[r][c+2], 
            board[r+1][c], board[r+1][c+1], board[r+1][c+2], 
            board[r+2][c], board[r+2][c+1], board[r+2][c+2]]
            if not check_duplicate(sq): 
                return False 

        return True 