# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self): 
        self.ans = float('-inf') 

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """ 
        The max path can be a line (non-bending) or a bending line (left child -> node -> right child) 
        but the DFS function cannot return bending paths, because connecting upper nodes to the root of the bend will not be valid.

        Hence the DFS return NON BENDING PATHS (node.val + max(left, right)) 
        and it updates ans through checking max bending paths (node.val + left + right). 
        Setting left and right to 0 if negative ensures including them will not be less optimal. 
        """ 

        def dfs(node): 
            if not node: return 0 

            left = dfs(node.left) 
            right = dfs(node.right) 

            # if left and right results in negative number, set them to 0 by excluding them 
            if left < 0: left = 0 
            if right < 0: right = 0 

            self.ans = max(self.ans, node.val + left + right)   # Update self.ans with bending path 
            return node.val + max(left, right)   # Non-bending path is returned for recursive use 
        
        dfs(root)
        return self.ans 