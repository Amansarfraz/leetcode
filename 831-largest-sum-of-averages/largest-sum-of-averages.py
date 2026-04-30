class Solution(object):
    def largestSumOfAverages(self, nums, k):
        n = len(nums)
        
        # Prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        # DP array
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        
        # Base case: 1 partition
        for i in range(1, n + 1):
            dp[i][1] = prefix[i] / float(i)
        
        # Fill DP
        for j in range(2, k + 1):
            for i in range(j, n + 1):
                for x in range(j-1, i):
                    dp[i][j] = max(
                        dp[i][j],
                        dp[x][j-1] + (prefix[i] - prefix[x]) / float(i - x)
                    )
        
        return dp[n][k]