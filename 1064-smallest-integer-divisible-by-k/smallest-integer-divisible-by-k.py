class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        
        # If k is divisible by 2 or 5,
        # a number containing only 1's can never divide it
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        remainder = 0
        
        # Try lengths from 1 to k
        for length in range(1, k + 1):
            
            # Build remainder of repunit incrementally
            remainder = (remainder * 10 + 1) % k
            
            # If remainder becomes 0,
            # current repunit is divisible by k
            if remainder == 0:
                return length
        
        return -1