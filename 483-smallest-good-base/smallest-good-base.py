class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        n = int(n)
        
        # Maximum length of the series
        max_m = n.bit_length()  # log2(n) + 1
        
        # Try each possible length m from largest to 1
        for m in reversed(range(1, max_m)):
            left, right = 2, n
            while left <= right:
                k = (left + right) // 2
                # Compute geometric sum: 1 + k + k^2 + ... + k^m
                s = (k**(m+1) - 1) // (k - 1)
                if s == n:
                    return str(k)
                elif s < n:
                    left = k + 1
                else:
                    right = k - 1
        
        # If no base found, smallest good base is n-1 (all ones in base n-1)
        return str(n - 1)