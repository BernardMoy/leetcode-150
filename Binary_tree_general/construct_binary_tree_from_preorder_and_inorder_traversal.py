# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """ 
        Visualise the recursion: 

        suppose pre = [3 20 15 7 9], in = [15 20 7 3 9]
        3 (first element of pre) is the root
        then all index before 3 inside in are the left tree, and all elements after are the right
        
        left = call recursion of ([20 15 7], [15 20 7])
        right = call recursion of ([9], [9])
        """

        if not inorder or not preorder: 
            return None 

        # Find the index of the root 
        root = preorder[0] 
        i = inorder.index(root) 

        # Create the tree with the root as root 
        tree = TreeNode(root) 
        
        # recursively compute the children of the current tree 
        tree.left = self.buildTree(preorder[1:1+i], inorder[:i])
        tree.right = self.buildTree(preorder[1+i:], inorder[i+1::])

        return tree 