class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        # dp[i][j] = max score difference current player can achieve
        dp = [[0] * n for _ in range(n)]
        
        # Base case: only one number left
        for i in range(n):
            dp[i][i] = nums[i]
        
        # Fill DP table
        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        
        return dp[0][n-1] >= 0