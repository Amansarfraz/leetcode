class Solution(object):
    def sortArrayByParity(self, nums):
        left = 0
        right = len(nums) - 1
        
        while left < right:
            
            # left should stop at odd
            while left < right and nums[left] % 2 == 0:
                left += 1
            
            # right should stop at even
            while left < right and nums[right] % 2 == 1:
                right -= 1
            
            nums[left], nums[right] = nums[right], nums[left]
        
        return nums