class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        import math

        # How many tests can we do
        tests = minutesToTest // minutesToDie + 1

        # Minimum pigs needed
        pigs = 0
        while tests ** pigs < buckets:
            pigs += 1

        return pigs