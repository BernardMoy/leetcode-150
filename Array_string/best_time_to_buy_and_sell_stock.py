class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Set a new l value when a smaller value is found,
        else update ans with max(ans, prices[r] - prices[l])
        """
        l = 0
        ans = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            elif prices[r] - prices[l] > ans:
                ans = prices[r] - prices[l]

        return ans
