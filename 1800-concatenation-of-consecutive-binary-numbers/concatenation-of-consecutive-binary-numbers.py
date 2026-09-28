class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        result = 0
        bit_length = 0
        
        for i in range(1, n + 1):
            # If i is a power of 2, its bit length increases by 1
            # (i & (i - 1)) == 0 checks if a number is a power of 2
            if (i & (i - 1)) == 0:
                bit_length += 1
                
            # Shift the running result by the bit length of i, then add i
            result = ((result << bit_length) + i) % MOD
            
        return result
