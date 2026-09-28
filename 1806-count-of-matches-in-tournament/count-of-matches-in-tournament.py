class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        # A tournament with n teams always requires n - 1 matches to find 1 winner.
        return n - 1
