class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # Remove dashes and convert to uppercase
        s = s.replace('-', '').upper()
        
        # Start from the end and build groups of size k
        res = []
        while s:
            res.append(s[-k:])
            s = s[:-k]
        
        # Reverse and join with dashes
        return '-'.join(res[::-1])