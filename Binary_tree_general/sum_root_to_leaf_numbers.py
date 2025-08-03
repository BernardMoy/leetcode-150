# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        TOP-DOWN DFS. 
        the top value will be multiplied by 10 when passed to lower levels. 
        """ 

        def dfs(node, val): 
            # base case leaf node (difficult part)
            if not node: 
                return 0

            # calculate new val by multiplying upper val *10
            new_val = val*10+ node.val 
            if not node.left and not node.right: 
                return val*10 + node.val  

            return dfs(node.left, new_val) + dfs(node.right, new_val) 
        
        return dfs(root, 0)