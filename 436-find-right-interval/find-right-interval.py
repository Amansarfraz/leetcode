class Solution(object):
    def findRightInterval(self, intervals):
        import bisect

        n = len(intervals)
        result = [-1] * n

        # Store start values with original indices
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))

        for i, (s, e) in enumerate(intervals):
            # Find smallest start >= end
            idx = bisect.bisect_left(starts, (e, 0))
            if idx < n:
                result[i] = starts[idx][1]

        return result