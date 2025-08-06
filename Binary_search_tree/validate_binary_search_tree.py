# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.previous = float("-inf")

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        For a valid BST, its inorder traversal should be sorted
        check this property while doing recursion calls
        by maintaining a previous variable.
        """
        # base case
        if not root:
            return True

        if not self.isValidBST(root.left):
            return False

        # root should be strictly greater than previous
        if root.val <= self.previous:
            return False

        # set self.previous to root
        self.previous = root.val
        return self.isValidBST(root.right)
