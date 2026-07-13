class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n <= 4:
            return 0

        nums.sort()

        return min(
            nums[-4] - nums[0],   # Remove 3 largest
            nums[-3] - nums[1],   # Remove 2 largest, 1 smallest
            nums[-2] - nums[2],   # Remove 1 largest, 2 smallest
            nums[-1] - nums[3]    # Remove 3 smallest
        )