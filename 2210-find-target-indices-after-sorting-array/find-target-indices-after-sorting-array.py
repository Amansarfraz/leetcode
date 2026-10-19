class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        less_than_target = 0
        equal_to_target = 0
        
        # Count how many elements are smaller than and equal to the target
        for num in nums:
            if num < target:
                less_than_target += 1
            elif num == target:
                equal_to_target += 1
        
        # Generate the indices based on the counts
        return [i for i in range(less_than_target, less_than_target + equal_to_target)]
