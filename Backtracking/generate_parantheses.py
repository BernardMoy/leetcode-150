class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        maintain two variables (open and closed) in the backtracking function
        When open < n, append ( 
        When closed < open, append ) 
        append -> backtrack -> pop while adding to the ans list 
        """

        ans = []
        s = []

        # Similar to DFS backtracking
        def backtrack(open, closed):

            # Matched
            if open == closed == n:
                ans.append("".join(s))
                return

            if open < n:
                # TRY adding open (EXPLORE space with open + 1)
                s.append('(')
                backtrack(open+1, closed)
                # Revoke action
                s.pop()

            if closed < open:
                # TRY adding closed
                s.append(')')
                backtrack(open, closed+1)
                s.pop()

        backtrack(0,0)

        return ans