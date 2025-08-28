class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Use bisect left binary search to find the position to insert. 

        After insertion, it can only cause the previous one interval to merge with it (since original is not overlapping) - check for that with if pos != 0. 
        Then, the pos is modified to become the starting position. 
        While overlapping with the next interval, merge them. 
        """

        if not intervals: 
            return [newInterval]

        pos = bisect_left(intervals, newInterval)

        def overlaps(i1, i2): 
            return i1[1] >= i2[0]
        
        def merge(i1, i2): 
            return [min(i1[0], i2[0]), max(i1[1], i2[1])]
        
        intervals.insert(pos, newInterval)
        if pos != 0 and overlaps(intervals[pos-1], intervals[pos]): 
            intervals[pos-1] = merge(intervals[pos-1], intervals[pos])
            intervals.pop(pos)
            pos -= 1

        while pos < len(intervals)-1 and overlaps(intervals[pos], intervals[pos+1]): 
            intervals[pos] = merge(intervals[pos], intervals[pos+1])
            intervals.pop(pos+1)
        
        return intervals