class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
        even_sum = 0
        
        for num in nums:
            if num % 2 == 0:
                even_sum += num
        
        result = []
        
        for val, index in queries:
            
            # Remove old value if even
            if nums[index] % 2 == 0:
                even_sum -= nums[index]
            
            # Update value
            nums[index] += val
            
            # Add new value if even
            if nums[index] % 2 == 0:
                even_sum += nums[index]
            
            result.append(even_sum)
        
        return result