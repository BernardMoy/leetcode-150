class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Greedy
        For each iteration, find the earliest index that satisfies nums[i] + i >= target.
        Then, update ans and target after finding it.
        """
        # base case
        if len(nums) == 1:
            return 0

        # target index is the last index
        target = len(nums) - 1
        ans = 0

        while target != 0:
            # Find the earliest index that can reach the end (target) position in one go
            cur = target
            for i in range(target, -1, -1):
                if nums[i] + i >= target:
                    cur = i

            # This count as one iteration
            target = cur
            ans += 1

        return ans
