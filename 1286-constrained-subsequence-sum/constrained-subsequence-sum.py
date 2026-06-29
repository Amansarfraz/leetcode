from collections import deque

class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * n
        dq = deque()
        ans = float("-inf")

        for i in range(n):
            while dq and dq[0] < i - k:
                dq.popleft()

            dp[i] = nums[i]
            if dq:
                dp[i] = max(dp[i], nums[i] + dp[dq[0]])

            ans = max(ans, dp[i])

            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()

            if dp[i] > 0:
                dq.append(i)

        return ans