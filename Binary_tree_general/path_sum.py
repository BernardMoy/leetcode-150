# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """ 
        Classic recursion with targetSum updated to targetSum - root.val
        """ 
        
        # Base cases 
        if not root: 
            return False 

        if not root.left and not root.right and root.val == targetSum: 
            return True 
        
        # Recursive case 
        if root.left and self.hasPathSum(root.left, targetSum - root.val): 
            return True 
        
        if root.right and self.hasPathSum(root.right, targetSum - root.val): 
            return True 
        
        return False 