# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Recursive solution that ensures nodes are modified in place: 
        Can be more efficient using preorder traversal

        The recursive helper function returns the flattened tree, and the rightmost node that is the most deep. 
        """
        if not root: 
            return root
        
        # helper function here 
        def helper(node): 
            # base case 
            if not node.left and not node.right: 
                return (node, node) 
            
            if not node.left: 
                r, rn = helper(node.right) 
                node.right = r 
                return (node, rn)
            
            if not node.right: 
                l, ln = helper(node.left) 
                node.left = None 
                node.right = l 
                return (node, ln)

            # flatten left and right separately 
            l, ln = helper(node.left) 
            r, rn = helper(node.right) 
            node.left = None 
            ln.right = r 
            node.right = l 
            return (node, rn) 
        
        f, fn = helper(root) 
        return f
