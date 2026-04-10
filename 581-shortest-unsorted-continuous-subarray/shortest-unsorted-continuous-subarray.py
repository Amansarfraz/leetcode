class Solution(object):
    def findUnsortedSubarray(self, nums):
        n = len(nums)
        left, right = -1, -2   # default for already sorted case
        max_seen = nums[0]
        min_seen = nums[-1]

        # left to right → find right boundary
        for i in range(n):
            max_seen = max(max_seen, nums[i])
            if nums[i] < max_seen:
                right = i

        # right to left → find left boundary
        for i in range(n - 1, -1, -1):
            min_seen = min(min_seen, nums[i])
            if nums[i] > min_seen:
                left = i

        return right - left + 1