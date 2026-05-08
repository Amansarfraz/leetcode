class Solution(object):
    def smallestRangeI(self, nums, k):
        diff = max(nums) - min(nums)
        
        return max(0, diff - 2 * k)