class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        get neighbours that return the number of live neighbours, then just add (i,j) to flip according to the rules. 
        """
        ROWS, COLS = len(board), len(board[0]) 

        def get_neighbours(board, i, j):
            nei = 0 
            if i > 0 and j > 0 and board[i-1][j-1] == 1: 
                nei += 1 
            if i > 0 and board[i-1][j] == 1: 
                nei += 1 
            if i > 0 and j < COLS-1 and board[i-1][j+1] == 1: 
                nei += 1 
            if j > 0 and board[i][j-1] == 1: 
                nei += 1 
            if i < ROWS-1 and j > 0 and board[i+1][j-1] == 1: 
                nei += 1 
            if i < ROWS-1 and board[i+1][j] == 1: 
                nei += 1 
            if i < ROWS-1 and j < COLS-1 and board[i+1][j+1] == 1: 
                nei += 1 
            if j < COLS-1 and board[i][j+1] == 1: 
                nei += 1  
            return nei 

        flips = [] 
        for i in range(ROWS): 
            for j in range(COLS): 
                neis = get_neighbours(board, i, j) 
                # rule 1
                if board[i][j] == 1 and neis < 2:
                    flips.append((i,j)) 

                # rule 2 
                if board[i][j] == 1 and neis in [2,3]: 
                    continue 

                # rule 3
                if board[i][j] == 1 and neis > 3: 
                    flips.append((i,j)) 

                # rule 4 
                if board[i][j] == 0 and neis == 3: 
                    flips.append((i,j)) 
        
        # flip all the positions listed 
        for i,j in flips: 
            board[i][j] = 1-board[i][j] 
        
        
                

