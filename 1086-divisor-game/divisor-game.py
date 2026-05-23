class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        # Alice wins only when n is even
        return n % 2 == 0