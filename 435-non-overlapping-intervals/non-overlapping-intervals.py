class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0
        
        # Sort by end time
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        end = float('-inf')
        
        for interval in intervals:
            if interval[0] >= end:
                # no overlap, keep it
                end = interval[1]
            else:
                # overlap → remove
                count += 1
        
        return count