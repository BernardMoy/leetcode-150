class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        Bottom up dp - starting at the lowest row, 
        each grid becomes val + min(dp(left), dp(right))
        until reach the top and return it. 

        The original triangle array can be used as space, resulting in O(1) extra space. 
        """ 
        # Base case 
        if len(triangle) == 1: 
            return triangle[0][0] 
        
        # Bottom up iteration
        for i in range(len(triangle)-2, -1, -1): 
            for j in range(len(triangle[i])): 
                # look for values in the following (i+1) row, left (j) or right (j+1) 
                triangle[i][j] = triangle[i][j] + min(triangle[i+1][j], triangle[i+1][j+1])
        
        return triangle[0][0]