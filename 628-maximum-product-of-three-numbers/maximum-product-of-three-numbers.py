class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        return max(
            nums[-1] * nums[-2] * nums[-3],  # 3 largest numbers
            nums[0] * nums[1] * nums[-1]     # 2 smallest (negative) + largest
        )