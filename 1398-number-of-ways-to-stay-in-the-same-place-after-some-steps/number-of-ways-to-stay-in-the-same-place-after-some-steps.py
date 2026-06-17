class Solution(object):
    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        max_pos = min(arrLen, steps + 1)
        dp = [0] * max_pos
        dp[0] = 1
        
        for _ in range(steps):
            new_dp = [0] * max_pos
            
            for i in range(max_pos):
                if dp[i]:
                    # stay
                    new_dp[i] = (new_dp[i] + dp[i]) % MOD
                    
                    # left
                    if i - 1 >= 0:
                        new_dp[i - 1] = (new_dp[i - 1] + dp[i]) % MOD
                    
                    # right
                    if i + 1 < max_pos:
                        new_dp[i + 1] = (new_dp[i + 1] + dp[i]) % MOD
            
            dp = new_dp
        
        return dp[0]