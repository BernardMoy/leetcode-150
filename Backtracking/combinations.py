class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        The backtrack function add the path to the ans
        By passing i+1 as the second recursive argument, this ensure no two number
        repeats in the path.
        """
        ans = []

        def backtrack(path, start):
            if len(path) == k:
                ans.append(path[:])
                return

            for i in range(start, n + 1):
                path.append(i)
                backtrack(path, i + 1)
                path.pop()

        backtrack([], 1)
        return ans
