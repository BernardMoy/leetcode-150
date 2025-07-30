# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """ 
        use null as the base case. 
        """ 
        if not p and not q: 
            return True 
        
        # not identical children 
        if (not p) and q or (not q) and p: 
            return False 
        
        # not identical value 
        if p.val != q.val: 
            return False 
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)