class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        # Ensure min_index comes before max_index
        if min_index > max_index:
            min_index, max_index = max_index, min_index

        # Case 1: Delete both from the left
        left = max_index + 1

        # Case 2: Delete both from the right
        right = n - min_index

        # Case 3: Delete min from left and max from right
        both = (min_index + 1) + (n - max_index)

        return min(left, right, both)