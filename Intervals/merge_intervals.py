class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Sort by start time.

        Merge two intervals by:
        if interval[0] <= previous[1]:
            prev[1] = max(prev[1], interval[1])
        """
        # sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        # iterate each interval
        ans = [intervals[0]]

        for interval in intervals[1::]:
            # check if the interval overlap with the last interval in ans
            if interval[0] <= ans[-1][1]:
                ans[-1][1] = max(
                    interval[1], ans[-1][1]
                )  # modify the last element in ans
            else:
                ans.append(interval)

        return ans
