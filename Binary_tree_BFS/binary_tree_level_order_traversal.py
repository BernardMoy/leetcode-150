# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Very generic BFS search using deque. 
        """ 

        # base case 
        if not root: 
            return [] 

        ans = [] 
        q = deque([root])

        while q: 
            row = [] 
            for _ in range(len(q)): 
                cur = q.popleft() 
                if not cur: 
                    continue 

                row.append(cur.val)
                q.append(cur.left) 
                q.append(cur.right)
            
            ans.append(row)
    
        return ans[:-1] 
                