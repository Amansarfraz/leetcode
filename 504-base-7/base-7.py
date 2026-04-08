class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        
        negative = num < 0
        num = abs(num)
        digits = []
        
        while num > 0:
            digits.append(str(num % 7))
            num //= 7
        
        # reverse digits and add negative sign if needed
        result = ''.join(digits[::-1])
        if negative:
            result = '-' + result
        
        return result