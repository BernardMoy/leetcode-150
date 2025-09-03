class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        Alternative to the question: For all Regions (connected by top left bottom right) that DOES NOT TOUCH THE BORDER, set all of them to X

        Then we can have a dfs function that expands a node, run it from all border elements, and change all unvisited Os to X. 
        """
        visited = set() 
        ROWS, COLS = len(board), len(board[0])
        
        # given (i,j) add ALL CONNECTED regions of (i,j) to the visited set. 
        def dfs(i,j): 
            if i < 0 or j < 0 or i == ROWS or j == COLS: 
                return 
            
            if board[i][j] == "X": 
                return 
            
            if (i,j) in visited: 
                return 

            visited.add((i,j))
            dfs(i-1, j) 
            dfs(i+1, j) 
            dfs(i, j+1) 
            dfs(i, j-1)
        
        # dfs on the 4 borders. 
        for j in range(COLS): 
            dfs(0, j) 
            dfs(ROWS-1, j) 
        
        for i in range(ROWS): 
            dfs(i, 0) 
            dfs(i, COLS-1) 
        
        # for all Os NOT in the visited set, set it to X. 
        for i in range(ROWS): 
            for j in range(COLS): 
                if board[i][j] == "O" and (i,j) not in visited: 
                    board[i][j] = "X"