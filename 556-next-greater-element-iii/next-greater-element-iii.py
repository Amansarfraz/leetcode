class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = list(str(n))
        i = len(digits) - 2
        
        # Step 1: find first decreasing digit
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
        
        if i < 0:
            return -1  # digits in descending order
        
        # Step 2: find the smallest digit > digits[i] to the right
        j = len(digits) - 1
        while digits[j] <= digits[i]:
            j -= 1
        
        # Step 3: swap
        digits[i], digits[j] = digits[j], digits[i]
        
        # Step 4: reverse the part after i
        digits[i + 1:] = reversed(digits[i + 1:])
        
        res = int(''.join(digits))
        return res if res <= 2**31 - 1 else -1