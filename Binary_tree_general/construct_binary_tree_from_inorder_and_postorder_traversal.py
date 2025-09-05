# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """ 
        Very similar to the previous (preorder and inorder) problem 
        where the root appears at the end of postorder instead of the front 

        note that the node values must be unique to be able to do this (.index())
        """ 

        if not inorder or not postorder: 
            return None 

        # Find the index of the root 
        root = postorder[-1] 
        i = inorder.index(root) 

        # Create the tree with the root as root 
        tree = TreeNode(root) 
        
        # recursively compute the children of the current tree 
        tree.right = self.buildTree(inorder[i+1::], postorder[i:-1])
        tree.left = self.buildTree(inorder[:i], postorder[:i] )

        return tree 