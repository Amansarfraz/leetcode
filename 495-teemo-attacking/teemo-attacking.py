class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        if not timeSeries:
            return 0
        
        total = 0
        
        for i in range(1, len(timeSeries)):
            gap = timeSeries[i] - timeSeries[i - 1]
            total += min(duration, gap)
        
        return total + duration