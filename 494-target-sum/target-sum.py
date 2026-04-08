class Solution(object):
    def findTargetSumWays(self, nums, target):
        total = sum(nums)
        
        # ❌ Not possible
        if (target + total) % 2 != 0 or abs(target) > total:
            return 0
        
        P = (target + total) // 2
        
        # 🔥 Subset sum count
        dp = [0] * (P + 1)
        dp[0] = 1
        
        for num in nums:
            for s in range(P, num - 1, -1):
                dp[s] += dp[s - num]
        
        return dp[P]