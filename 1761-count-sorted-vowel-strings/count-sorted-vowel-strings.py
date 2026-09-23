class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Using the stars and bars combinatorics formula: (n + 4) choose 4
        return (n + 4) * (n + 3) * (n + 2) * (n + 1) // 24
