# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        For a complete binary tree, if left height = right height,
        its height is 2**left height - 1
        """

        # function to calculate the left and right tree height
        def left_height(node):
            if not node:
                return 0
            else:
                return 1 + left_height(node.left)

        def right_height(node):
            if not node:
                return 0
            else:
                return 1 + right_height(node.right)

        if left_height(root) == right_height(root):
            return 2 ** left_height(root) - 1
        else:
            # Call the function recursively
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
