class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 0:
            return 1
        
        mask = 1
        
        while mask <= n:
            mask <<= 1
        
        return (mask - 1) ^ n