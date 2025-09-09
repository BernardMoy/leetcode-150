class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """ 
        DFS function that slice the word using [1::] 

        To keep track of a visited set to prevent visiting same grid back and fourth
        add to set -> dfs current node -> remove from set  (Backtracking here) 

        because subsequent dfs recursive calls can add to the visited set.         
        """ 

        ROWS, COLS = len(board), len(board[0])
        visited = set() 

        # prevent visiting same grid multiple times 
        def dfs(i,j, word): 
            if (i,j) in visited: 
                return False 
            
            # if the starting pos (i,j) is not word[0] this is invalid 
            if board[i][j] != word[0]: 
                return False 
                
            # matched end of the word 
            if len(word) == 1 and board[i][j] == word[0]: 
                return True 
            
            # dfs its possible neighbours 
            visited.add((i,j)) 

            nei = [] 
            if i > 0:
                nei.append((i-1, j)) 
            if j < COLS-1: 
                nei.append((i, j+1)) 
            if i < ROWS-1:
                nei.append((i+1, j)) 
            if j > 0:
                nei.append((i, j-1)) 
            
            for a,b in nei: 
                if dfs(a,b,word[1::]): 
                    return True 
            
            visited.remove((i,j))
            return False 
        
        # try dfs starting from each position
        for i in range(ROWS): 
            for j in range(COLS): 
                if dfs(i,j,word): 
                    return True 
        
        return False 