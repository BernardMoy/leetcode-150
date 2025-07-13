class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0 
        ans = 0 
        for i in range(len(prices)-1): 
            # Greedily buy stock and then sell them the next day 
            if prices[i] < prices[i+1]: 
                ans += prices[i+1] - prices[i] 
        
        return ans 