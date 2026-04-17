class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        
        prod = 1
        left = 0
        count = 0
        
        for right in range(len(nums)):
            prod *= nums[right]
            
            # shrink window if product >= k
            while prod >= k:
                prod //= nums[left]
                left += 1
            
            # count subarrays ending at right
            count += (right - left + 1)
        
        return count