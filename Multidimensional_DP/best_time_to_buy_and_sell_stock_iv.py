class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """ 
        Refer to the III problem (extend the same logic) 
        buy depends on the results previously sold and sell depends on the value spent 
        """ 
        
        # Base case no transactions 
        if k == 0: 
            return 0  
        
        # 2 DP memo tables 
        buys = [float('inf') for _ in range(k+1)] 
        gains = [0 for _ in range(k+1)] 

        for price in prices: 
            for i in range(1, k+1): 
                buys[i] = min(buys[i], price-gains[i-1])
                gains[i] = max(gains[i], price-buys[i])
        
        return gains[k]