# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        classic dfs
        dfs left, dfs right, and then take their maximum
        """

        # base case
        if not root:
            return 0

        def dfs(root, cur):
            # check leaf
            if not root or not root.left and not root.right:
                return cur

            a = dfs(root.left, cur + 1)
            b = dfs(root.right, cur + 1)
            return max(a, b)

        return dfs(root, 1)
