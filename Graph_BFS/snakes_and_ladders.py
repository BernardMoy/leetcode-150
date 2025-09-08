class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """ 
        Helper function to get the board value when given a "number" as specified in the question.
        Queue BFS (~shortest path problem). 
        use a visited set to keep track of already visited nodes because subsequent visits are always less optimal (take more steps for the same pos). 
        """ 
        
        # first reverse the board 
        board.reverse() 
        N = len(board)

        # function to return the value from the board when given a position number 
        def get(value): 
            r = (value-1)//N
            c = (value-1)%N 

            # odd number rows are reverse 
            if r % 2 == 1: 
                c = N-c-1
            
            return board[r][c] 
        
        # queue for BFS to store (positionNumber, numberSteps) 
        q = deque([(1,0)])
        visited = set() 

        while q: 
            pos, step = q.popleft() 
            for i in range(1,7): 
                new = pos + i 

                # teleport to the specified value if not -1 
                if get(new) != -1: 
                    new = get(new) 
                
                # reached end 
                if new == N*N: 
                    return step + 1 
                
                if new not in visited: 
                    visited.add(new) 
                    q.append((new, step+1)) # increment steps here 
        
        return -1 
