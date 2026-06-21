class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        n = len(palindrome)
        
        # Edge case: single character
        if n == 1:
            return ""
        
        s = list(palindrome)
        
        # Try to make it lexicographically smallest
        for i in range(n // 2):
            if s[i] != 'a':
                s[i] = 'a'
                return "".join(s)
        
        # If all are 'a', change last char
        s[-1] = 'b'
        return "".join(s)