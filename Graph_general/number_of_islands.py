class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Number of connected components problem
        The add() function is a recursive function that adds coordinates into the visited set.
        """

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        ans = 0

        def add(i, j):
            # Skip if out of bounds or visited
            if i < 0 or j < 0 or i == ROWS or j == COLS or (i, j) in visited:
                return

            # Skip if grid is water
            if grid[i][j] == "0":
                return

            visited.add((i, j))

            # Recursive calls for 4 sides
            add(i - 1, j)
            add(i, j - 1)
            add(i + 1, j)
            add(i, j + 1)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == "1":
                    ans += 1
                    add(r, c)

        return ans
