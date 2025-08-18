class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        For a valid square to exist, it has to satisfy:
        the value to the right, the value down, and the diagonal value have to be 1
        then 1 can be added to it to create a larger square.

        i.e. Bottom up DP -> matrix[r][c] = 1+min(
                        int(matrix[r+1][c+1]),
                        int(matrix[r][c+1]),
                        int(matrix[r+1][c])
                    )
                    if matrix[r][c] == 1.
        """

        ROWS, COLS = len(matrix), len(matrix[0])

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if r == ROWS - 1 or c == COLS - 1:
                    matrix[r][c] = int(matrix[r][c])

                elif matrix[r][c] == "1":
                    matrix[r][c] = 1 + min(
                        int(matrix[r + 1][c + 1]),
                        int(matrix[r][c + 1]),
                        int(matrix[r + 1][c]),
                    )

                else:
                    matrix[r][c] = int(matrix[r][c])

        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                ans = max(ans, matrix[r][c] * matrix[r][c])

        return ans
