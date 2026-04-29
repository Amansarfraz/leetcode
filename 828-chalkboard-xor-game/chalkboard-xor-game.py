class Solution(object):
    def xorGame(self, nums):
        total_xor = 0
        
        for num in nums:
            total_xor ^= num
        
        if total_xor == 0:
            return True
        
        return len(nums) % 2 == 0