"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """ 
        Use a dict to map the old nodes to the new nodes (as node.val is unique)
        and use the dict as the visited set at the same time. 
        Because of this we can recursively call DFS on the neighbours of the copied node. 
        """ 
        
        if not node: 
            return None 

        # Dict to map the original nodes to the copied nodes 
        d = {} 

        def dfs(node): 
            # if node already in d, return the new node 
            if node.val in d: 
                return d[node.val] 
            
            # Else create a copy of the node 
            copy = Node(node.val) 

            # Add it to the dict to mark it as visited 
            d[node.val] = copy 
            for neighbor in node.neighbors: 
                copy.neighbors.append(dfs(neighbor)) 
            
            return copy 

        return dfs(node) 
