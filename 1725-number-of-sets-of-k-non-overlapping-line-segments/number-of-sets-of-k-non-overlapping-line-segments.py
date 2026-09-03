class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # dp[j] will store the number of ways to form j segments
        dp = [0] * (k + 1)
        dp[0] = 1 # Base case: 1 way to form 0 segments
        
        # running_sum[j] stores the accumulated ways to transition into j segments
        running_sum = [0] * (k + 1)
        
        for i in range(1, n):
            for j in range(k, 0, -1):
                # Update the running sum with the configurations from the previous point
                running_sum[j] = (running_sum[j] + dp[j-1]) % MOD
                # Add the segments that end exactly at point i
                dp[j] = (dp[j] + running_sum[j]) % MOD
                
        return dp[k]
