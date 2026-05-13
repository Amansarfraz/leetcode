class Solution(object):
    def maxWidthRamp(self, nums):
        n = len(nums)
        stack = []

        # Step 1: build decreasing stack of indices
        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        res = 0

        # Step 2: check from right
        for j in range(n - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                i = stack.pop()
                res = max(res, j - i)

        return res