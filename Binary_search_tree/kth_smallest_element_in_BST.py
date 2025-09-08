# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self): 
        self.count = 0 

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """ 
        Design a helper function that returns a value if within k, else return null. 
        Traverse the left side, increment count, then traverse the right side, 
        because it should not cost any k decrements to travel to the left side (~start there). 

        Note that must explicitly say if left is not None instead of "if left" (0 is falsy value) 
        Note that the count variable must be global, and cannot be passed into functions 

        This would be more efficient than doing a full inorder traversal (in sorted order). 
        """ 

        def helper(node): 
            if not node: 
                return

            # count left side first, then right side 
            left = helper(node.left) 
            # if the left side generated a result, return it 
            if left is not None:    # <-- MUST explicitly say "is not None" here as 0 is falsy value 
                return left 
            
            # increment count here 
            self.count += 1 
            if self.count == k: 
                return node.val 

            # then do the right side 
            right = helper(node.right) 
            if right is not None: 
                return right 

        return helper(root) 