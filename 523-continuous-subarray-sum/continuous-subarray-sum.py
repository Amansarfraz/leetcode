class Solution(object):
    def checkSubarraySum(self, nums, k):
        mods = {0: -1}  # prefix sum modulo k -> first index
        prefix_sum = 0
        
        for i, num in enumerate(nums):
            prefix_sum += num
            if k != 0:
                prefix_sum %= k
            
            if prefix_sum in mods:
                if i - mods[prefix_sum] >= 2:
                    return True
            else:
                mods[prefix_sum] = i
        
        return False