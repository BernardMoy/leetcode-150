class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """ 
        Classic bottom up DP problem 
        dp[i][j] = dp[i-1][j] + dp[i][j-1] if no obstacle, else = 0
        """ 

        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        memo = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        # Set the top left corner of memo table to be 1 
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            memo[0][0] = 1

        for r in range(ROWS):
            for c in range(COLS):
                # skip the top left corner 
                if r == 0 and c == 0: 
                    continue 

                if obstacleGrid[r][c] != 1:
                    top = memo[r-1][c] if r > 0 else 0
                    left = memo[r][c-1] if c > 0 else 0
                    memo[r][c] = top + left

        return memo[-1][-1] 