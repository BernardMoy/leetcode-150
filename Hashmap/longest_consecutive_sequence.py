class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Use a while loop to check for consecutive sequences in a set.
        Compared to O(n log n) sorting first, this method can do it in O(n)
        """

        # base case
        if not nums:
            return 0

        s = set(nums)
        ans = 1

        for n in s:
            # Ensure that n is the smallest element (start) of a sequence in s
            if n - 1 in s:
                continue

            # use a while loop to check for consecutive sequences
            cur = 1
            while n + 1 in s:
                n += 1
                cur += 1

            ans = max(ans, cur)

        return ans
