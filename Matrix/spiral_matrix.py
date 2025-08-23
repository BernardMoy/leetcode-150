class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Maintain i iterator that alternates between right, bottom, left, top
        and use 4 variables to keep track of the current top, bottom, left, right positions.
        At the end, only return up to ROWS*COLS as the latter iterations are repeated.
        """

        ROWS, COLS = len(matrix), len(matrix[0])

        top = 0
        bottom = ROWS - 1
        left = 0
        right = COLS - 1

        ans = []
        while len(ans) < ROWS * COLS:
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            for i in range(right, left - 1, -1):
                ans.append(matrix[bottom][i])
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1

        return ans[: ROWS * COLS]
