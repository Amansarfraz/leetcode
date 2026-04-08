class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        # Convert time to minutes
        minutes = []
        for t in timePoints:
            h, m = map(int, t.split(":"))
            minutes.append(h * 60 + m)
        
        minutes.sort()
        min_diff = float('inf')
        
        # Compare consecutive times
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i-1])
        
        # Wrap-around case (from last to first time)
        min_diff = min(min_diff, 1440 - (minutes[-1] - minutes[0]))
        
        return min_diff