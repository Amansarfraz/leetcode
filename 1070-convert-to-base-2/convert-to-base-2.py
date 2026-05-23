class Solution(object):
    def baseNeg2(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        # Special case
        if n == 0:
            return "0"
        
        result = []
        
        while n != 0:
            
            # Get remainder
            remainder = n % -2
            n = n // -2
            
            # Fix negative remainder
            if remainder < 0:
                remainder += 2
                n += 1
            
            result.append(str(remainder))
        
        # Reverse to get final answer
        return ''.join(result[::-1])