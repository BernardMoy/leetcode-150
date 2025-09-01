# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """ 
        Super generic BFS queue 
        that appends current level in reverse order depending on the parity of level 
        """ 

        q = deque([root]) 
        ans = [] 
        while q: 
            arr = []  # temp array to store the values of current level 
            for _ in range(len(q)): 
                cur = q.popleft() 
                if not cur: 
                    continue 
                arr.append(cur.val) 
                q.append(cur.left) 
                q.append(cur.right) 
            
            # zigzag order here 
            if arr: 
                if len(ans) % 2 == 1: 
                    ans.append(arr[::-1]) 
                else: 
                    ans.append(arr)
        
        return ans