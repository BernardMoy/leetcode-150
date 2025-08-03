class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Classic top down DP 
        returns -1 if invalid, so this needs to be checked for each recursive call. 
        """ 
        
        if amount in self.memo:
            return self.memo[amount]

        if amount<0:
            return -1
        if amount == 0:
            return 0
        
        # recursive
        m = -1
        for c in coins:
            r = self.coinChange(coins, amount-c)
            if r != -1:
                if m == -1:
                    m = r+1
                else:
                    m = min(m, r+1)
        
        self.memo[amount] = m
        return m
            