"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        """ 
        main point: dfs that takes in the top and left coord and the size to explore 
        (-> divide and conquer by adding to top and left) 

        Can simply use a for loop to check if all its child are equal in the conquer step. 
        """ 

        N = len(grid) 
        def dfs(top, left, size): 
            # base case: size = 1 
            if size == 1: 
                return Node(grid[top][left], True)  # mark the isLeaf property as True 
            
            # recursively call dfs with size // 2 
            tl = dfs(top, left, size//2) 
            tr = dfs(top, left+size//2, size//2) 
            bl = dfs(top+size//2, left, size//2) 
            br = dfs(top+size//2, left+size//2, size//2) 

            # if all children have the same value, group them into a single leaf 
            a = True 
            for child in [tl, tr, bl, br]: 
                if not (child.isLeaf and child.val == tl.val): 
                    a = False 
                    break 
            
            if a: 
                return Node(tl.val, True) 
            else: 
                return Node(tl.val, False, tl, tr, bl, br)
        
        return dfs(0,0,N)