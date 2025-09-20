class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """ 
        Use 2 nested for loops to check how many points are with the same SLOPE with the CURRENT point
        If 2 other points are on the same slope with a current point, these 3 points must be on same straight line
        
        Note that the vertical slope case also have to be considered -> occur when a == a2 
        """ 

        ans = 0 
        for a,b in points: 
            d = defaultdict(float)  
            for a2, b2 in points: 
                if a == a2 and b == b2: continue 
                if a == a2:
                    d['straight'] += 1 
                else: 
                    d[(b2-b)/(a2-a)] += 1 
            
            # find the max value (most frequently occurred slope) 
            m = max((value for key, value in d.items()), default = 0) 
            ans = max(ans, m) 
        
        return int(ans) + 1  # +1 including the point itself 