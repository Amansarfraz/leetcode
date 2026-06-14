class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        dp = {}
        ans = 0

        for num in arr:
            dp[num] = dp.get(num - difference, 0) + 1
            ans = max(ans, dp[num])

        return ans