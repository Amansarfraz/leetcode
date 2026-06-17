class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0, float('-inf'), float('-inf')]
        
        for num in nums:
            temp = dp[:]
            
            for r in range(3):
                temp[(r + num) % 3] = max(
                    temp[(r + num) % 3],
                    dp[r] + num
                )
            
            dp = temp
        
        return dp[0]