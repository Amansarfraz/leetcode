class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
            
        # Start writing from index 2 since the first two elements are always allowed
        write_index = 2
        
        for read_index in range(2, len(nums)):
            # Compare current element with the element written two places back
            if nums[read_index] != nums[write_index - 2]:
                nums[write_index] = nums[read_index]
                write_index += 1
                
        return write_index
