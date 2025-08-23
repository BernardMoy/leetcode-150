class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Transpose the matrix, then swap it along vertical axis.

        Iterate over all i, j in range(N) while i < j, then swap every value,
        to achieve transposing matrix in place.
        """

        # Transpose matrix code
        N = len(matrix)
        for i in range(N):
            for j in range(i + 1, N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Swap matrix along vertical axis
        for i in range(N):
            for j in range(N // 2):
                matrix[i][j], matrix[i][N - 1 - j] = matrix[i][N - 1 - j], matrix[i][j]

        return matrix
