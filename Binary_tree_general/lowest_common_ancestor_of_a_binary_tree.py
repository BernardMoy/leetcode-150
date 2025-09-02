# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """ 
        If a common ancestor is found, then dfs() should return a value for both the left subtree and right subtree 
        otherwise if the node.val does not exist in that branch, null is returned 
        """ 
        def dfs(node): 
            # Base case (all values are unique)
            if not node: 
                return None 
            if node.val == p.val or node.val == q.val: 
                return node 
            
            left = dfs(node.left) 
            right = dfs(node.right) 

            if left and right: 
                return node 
            
            return left if left else right 
        
        return dfs(root)
