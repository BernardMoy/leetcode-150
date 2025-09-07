# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    """ 
    Instead of listing out the inorder traversal, simulate it step by step 
    can be achieved by a pushall function that traverses to the leftmost bottommost point, 
    then pop back the stack to consider the right child - effectively doing inorder traversal. 
    """ 
    def __init__(self, root: Optional[TreeNode]):
        self.stx = [root] 

        # add all left child of the root (to the deepest level) to the stx 
        cur = root 
        while cur.left: 
            self.stx.append(cur.left) 
            cur = cur.left 

    # custom method to push all the left child of node to the stack in order 
    def pushall(self, node): 
        cur = node 
        while cur: 
            self.stx.append(cur) 
            cur = cur.left 

    def next(self) -> int:
        if not self.stx: 
            return None 

        elem = self.stx.pop()
        
        # if the latest element have right child, then recursively simulate the DFS 
        # by pushing all leftmost elements of that child
        if elem.right: 
            self.pushall(elem.right) 
        
        return elem.val 
        
        
    def hasNext(self) -> bool:
        return len(self.stx) != 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()