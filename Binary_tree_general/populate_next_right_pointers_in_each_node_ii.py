"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        Classic BFS: use a level array to maintiain the current level 
        then set the next pointers after each level has been traversed 
        """
        
        q = deque([root])
        level = [] 

        while q: 
            level.clear() 
            for _ in range(len(q)): 
                cur = q.popleft() 
                if not cur: 
                    continue 

                level.append(cur) 
                if cur.left: 
                    q.append(cur.left) 
                if cur.right: 
                    q.append(cur.right)
            
            # populate next right pointers here 
            level.append(None) 
            for i in range(len(level)-1): 
                level[i].next = level[i+1] 
        
        return root 