class Solution(object):
    def partitionDisjoint(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_max = nums[0]
        curr_max = nums[0]
        pos = 0

        for i in range(1, len(nums)):
            curr_max = max(curr_max, nums[i])

            if nums[i] < left_max:
                left_max = curr_max
                pos = i

        return pos + 1