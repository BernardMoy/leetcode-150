class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ 
        Maintain 4 variables (buy is negative, sell is positive) 
        simulate the sequence of first buy and sell and second buy and sell 
        sell1 adds the current price to buy1, buy2 to sell1.. etc
        """ 

        buy1 = -prices[0] 
        sell1 = 0 
        buy2 = -prices[0] 
        sell2 = 0 

        for price in prices: 
            buy1 = max(buy1, -price) 
            sell1 = max(sell1, buy1+price) 
            buy2 = max(buy2, sell1-price) 
            sell2 = max(sell2, buy2+price) 
        
        return sell2 