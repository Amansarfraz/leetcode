class Solution(object):
    def minimumOneBitOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        # Gray code to binary conversion
        while n > 0:
            ans ^= n
            n >>= 1
        return ans
