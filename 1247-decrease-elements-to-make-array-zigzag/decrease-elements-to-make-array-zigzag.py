class Solution(object):
    def movesToMakeZigzag(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = [0, 0]

        for i in range(n):
            left = nums[i - 1] if i > 0 else float('inf')
            right = nums[i + 1] if i < n - 1 else float('inf')

            decrease = max(0, nums[i] - min(left, right) + 1)

            res[i % 2] += decrease

        return min(res)