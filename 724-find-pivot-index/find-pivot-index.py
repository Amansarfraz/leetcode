class Solution(object):
    def pivotIndex(self, nums):
        total = sum(nums)
        left_sum = 0
        
        for i in range(len(nums)):
            # right sum = total - left_sum - nums[i]
            if left_sum == total - left_sum - nums[i]:
                return i
            
            left_sum += nums[i]
        
        return -1