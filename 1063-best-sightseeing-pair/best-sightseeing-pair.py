class Solution(object):
    def maxScoreSightseeingPair(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        
        best = values[0]
        ans = 0
        
        for j in range(1, len(values)):
            ans = max(ans, best + values[j] - j)
            best = max(best, values[j] + j)
        
        return ans