class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Refer to "container with the most water" 
        maintain two pointers, and move the one with LOWER current height. 
        That lower pillar is limiting how many water we can trap 
        """
        
        l, r = 0, len(height)-1
        ans = 0 
        lmax, rmax = height[0], height[-1] 

        while l < r: 
            # greedily move the pillar with lower height 
            if height[l] < height[r]: 
                l += 1 
                lmax = max(lmax, height[l]) 
                ans += lmax-height[l]   # the width is 1 (iterating 1 at a time), this is the height
            
            else: 
                r -= 1 
                rmax = max(rmax, height[r]) 
                ans += rmax-height[r] 
        
        return ans 