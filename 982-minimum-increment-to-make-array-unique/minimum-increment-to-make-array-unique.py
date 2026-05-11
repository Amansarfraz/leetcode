class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        moves = 0
        curr = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] <= curr:
                curr += 1
                moves += curr - nums[i]
            else:
                curr = nums[i]
        
        return moves