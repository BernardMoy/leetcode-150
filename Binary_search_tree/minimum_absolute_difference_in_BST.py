# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        Remember preorder traversal of a binary search tree is sorted
        Difference must occur between two consecutive sorted items. 
        """ 

        def preorder(node): 
            if not node.left and not node.right: 
                return [node.val]
            
            if not node.left: 
                return [node.val] + preorder(node.right) 
            if not node.right: 
                return preorder(node.left) + [node.val]
            
            return preorder(node.left) + [node.val] + preorder(node.right)
        
        ans = float('inf')
        nodes = preorder(root) 
        for i in range(len(nodes)-1):
            ans = min(ans, nodes[i+1]-nodes[i])
        
        return ans 