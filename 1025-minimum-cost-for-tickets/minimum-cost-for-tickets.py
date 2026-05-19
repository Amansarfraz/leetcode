class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        
        n = len(days)
        dp = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            
            # 1-day pass
            j1 = i
            while j1 < n and days[j1] < days[i] + 1:
                j1 += 1
            
            # 7-day pass
            j7 = i
            while j7 < n and days[j7] < days[i] + 7:
                j7 += 1
            
            # 30-day pass
            j30 = i
            while j30 < n and days[j30] < days[i] + 30:
                j30 += 1
            
            dp[i] = min(
                costs[0] + dp[j1],
                costs[1] + dp[j7],
                costs[2] + dp[j30]
            )
        
        return dp[0]