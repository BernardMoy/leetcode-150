class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """ 
        Sort the intevals by START time. 

        Then, maintain a current overlapping interval region: (1,6)(2,8) -> (2,6) 
        If a new interval does not overlap with that, increase the ans (need a separate arrow)
        """ 
        # sort the intervals by start time 
        points.sort(key = lambda x: x[0]) 

        # maintain the overlapping region of intervals 
        cur = points[0]
        ans = 1

        for i in range(1, len(points)): 
            if cur[1] >= points[i][0]: 
                cur[0] = min(cur[0], points[i][0]) 
                cur[1] = min(cur[1], points[i][1]) 
            
            else: 
                cur = points[i]
                ans += 1 
        
        return ans 