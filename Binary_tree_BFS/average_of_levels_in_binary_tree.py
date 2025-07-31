# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        classic BFS
        """
        q = deque([root])
        ans = []

        while q:
            total = 0
            count = 0
            for _ in range(len(q)):
                cur = q.popleft()
                total += cur.val
                count += 1

                # append children
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)

            ans.append(total / count)

        return ans
