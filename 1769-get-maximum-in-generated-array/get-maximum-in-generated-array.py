class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Base cases for n = 0 and n = 1
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        # Initialize the array up to index n
        nums = [0] * (n + 1)
        nums[1] = 1
        
        # Track the maximum value found
        max_val = 1
        
        # Fill the array following the problem's rules
        for i in range(1, (n // 2) + 1):
            if 2 * i <= n:
                nums[2 * i] = nums[i]
                max_val = max(max_val, nums[2 * i])
                
            if 2 * i + 1 <= n:
                nums[2 * i + 1] = nums[i] + nums[i + 1]
                max_val = max(max_val, nums[2 * i + 1])
                
        return max_val
