class Solution(object):
    def kInversePairs(self, n, k):
        MOD = 10**9 + 7
        
        dp = [0] * (k + 1)
        dp[0] = 1
        
        for i in range(1, n + 1):
            new_dp = [0] * (k + 1)
            prefix_sum = 0
            
            for j in range(0, k + 1):
                prefix_sum += dp[j]
                
                if j >= i:
                    prefix_sum -= dp[j - i]
                
                new_dp[j] = prefix_sum % MOD
            
            dp = new_dp
        
        return dp[k]