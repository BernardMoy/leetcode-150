# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Recursive solution requires
        dfs(left.right, right.left) and dfs(left.left, right.right)
        to be satisfied. This ensures it is actually mirrored

        For the iterative solution, BFS and use a queue. For each layer use a stack to check for 'palindrome'
        """

        # Base case
        if not root:
            return False

        # dfs recursive function
        def dfs(left, right):
            # base case: both null
            if not left and not right:
                return True

            # unequal number of children
            if left and not right or right and not left:
                return False

            # unequal value
            if left.val != right.val:
                return False

            # cross dfs
            return dfs(left.right, right.left) and dfs(left.left, right.right)

        return dfs(root.left, root.right)
