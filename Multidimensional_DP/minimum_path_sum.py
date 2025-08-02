class Solution:
    def minPathSum(self, grid):

        """
        Bottom up DP
        Top down DP would require a very large key, or the position (i,j) as the key 

        Use an extra row to prevent overflow, 
        and start at the bottom right to work upwards to [0][0]

        Use two for loops to iterate the rows and cols index backwards.
        """
        # MEMO TABLE
        rows = len(grid)
        cols = len(grid[0])

        memo = [[float('inf')]*(cols+1) for i in range(rows+1)]   # Extra row to prevent exceed index
        memo[rows][cols-1] = 0
        memo[rows-1][cols] = 0

        for row in range(rows-1, -1, -1):
            for col in range(cols-1, -1, -1):
                memo[row][col] = grid[row][col] + min(memo[row+1][col], memo[row][col+1])

        return memo[0][0]