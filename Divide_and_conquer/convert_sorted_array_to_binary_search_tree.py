# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Classic divide and conquer problem
        where the center is len(nums) // 2
        """

        # base case
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0], None, None)

        # Find the middle index
        mid = len(nums) // 2

        # recursively construct left and right
        l = self.sortedArrayToBST(nums[:mid])
        r = self.sortedArrayToBST(nums[mid + 1 :])
        return TreeNode(nums[mid], l, r)
