class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Greedy algorithm that iterates backwards. 
        Target represent the latest (rightmost) index that can reach the last position. 
        return target == 0 means whether it is reachable from the start. 
        """ 
        
        # target index is the last index 
        target = len(nums) - 1

        # Iterate backwards to greedily select the possible path 
        for i in range(len(nums)-1, -1, -1): 
            if nums[i] + i >= target: 
                target = i 
        
        # As long as the last index is reachable from that position, 
        # target is set to the index value 
        return target == 0 