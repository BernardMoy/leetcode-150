# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        BFS using a queue.
        After each iteration, add the last element of the queue to the ans.
        """

        if not root:
            return []

        ans = [root.val]

        q = deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # extract the last element and add to ans
            if q:
                ans.append(q[-1].val)

        return ans
