class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        
        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i + 1]
            res.extend([val] * freq)
        
        return res