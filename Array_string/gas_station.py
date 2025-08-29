class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Maintain a difference array, and iterate it 
        greedily set the next index to be the start, if a negative sum is encountered in the middle of iteration (That is not allowed)
        """
        # base case: sum(gas) >= sum(cost) 
        if sum(cost) > sum(gas): 
            return -1 

        total = 0 
        ans = 0 
        for i in range(len(gas)): 
            total += (gas[i]-cost[i])

            # if total < 0, set the starting index to the next one 
            if total<0: 
                total = 0 
                ans = i+1 
        
        return ans 