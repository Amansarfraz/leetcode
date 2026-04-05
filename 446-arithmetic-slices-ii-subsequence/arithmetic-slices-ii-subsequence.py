class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        dp = [{} for _ in range(n)]
        res = 0
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                
                count = dp[j].get(diff, 0)
                
                res += count
                
                dp[i][diff] = dp[i].get(diff, 0) + count + 1
        
        return res