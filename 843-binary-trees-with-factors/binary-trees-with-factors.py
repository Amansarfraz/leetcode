class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        MOD = 10**9 + 7
        arr.sort()
        
        dp = {}
        
        for i, x in enumerate(arr):
            dp[x] = 1  # single node
            
            for j in range(i):
                a = arr[j]
                if x % a == 0:
                    b = x // a
                    if b in dp:
                        dp[x] += dp[a] * dp[b]
            
            dp[x] %= MOD
        
        return sum(dp.values()) % MOD