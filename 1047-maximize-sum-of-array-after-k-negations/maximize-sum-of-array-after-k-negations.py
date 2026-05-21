class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        nums.sort()
        
        i = 0
        
        while i < len(nums) and k > 0 and nums[i] < 0:
            nums[i] = -nums[i]
            i += 1
            k -= 1
        
        total = sum(nums)
        
        if k % 2 == 1:
            total -= 2 * min(nums)
        
        return total