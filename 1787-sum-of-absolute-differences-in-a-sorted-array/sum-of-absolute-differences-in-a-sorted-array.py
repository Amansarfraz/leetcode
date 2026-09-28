class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        total_sum = sum(nums)
        left_sum = 0
        result = []
        
        for i, num in enumerate(nums):
            # Calculate right sum dynamically using total sum and left sum
            right_sum = total_sum - left_sum - num
            
            left_count = i
            right_count = n - 1 - i
            
            # Compute absolute difference totals for both partitions
            left_diff = (num * left_count) - left_sum
            right_diff = right_sum - (num * right_count)
            
            result.append(left_diff + right_diff)
            
            # Update left sum for the next iteration
            left_sum += num
            
        return result
