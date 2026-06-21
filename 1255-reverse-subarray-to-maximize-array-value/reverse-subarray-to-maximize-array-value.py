class Solution(object):
    def maxValueAfterReverse(self, nums):
        n = len(nums)

        # Step 1: base sum
        base = 0
        for i in range(n - 1):
            base += abs(nums[i] - nums[i + 1])

        # Step 2: edge improvement
        gain = 0
        for i in range(n - 1):
            gain = max(gain,
                       abs(nums[0] - nums[i + 1]) - abs(nums[i] - nums[i + 1]),
                       abs(nums[-1] - nums[i]) - abs(nums[i] - nums[i + 1]))

        # Step 3: middle optimization
        min_max = float('inf')
        max_min = float('-inf')

        for i in range(n - 1):
            a, b = nums[i], nums[i + 1]
            min_max = min(min_max, max(a, b))
            max_min = max(max_min, min(a, b))

        gain = max(gain, 2 * (max_min - min_max))

        return base + gain