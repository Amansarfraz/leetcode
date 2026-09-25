class Solution(object):
    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # Start by assuming all 'n' characters are 'a' (value 1)
        res = ['a'] * n
        k -= n  # Subtract the value of 'n' 'a's from k
        
        # Fill with 'z' from right to left as much as possible
        i = n - 1
        while k > 0:
            add = min(25, k)
            res[i] = chr(ord('a') + add)
            k -= add
            i -= 1
            
        return "".join(res)
