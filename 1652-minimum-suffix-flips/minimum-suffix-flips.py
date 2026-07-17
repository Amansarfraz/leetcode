class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        flips = 0

        for ch in target:
            if (flips % 2 == 0 and ch == '1') or (flips % 2 == 1 and ch == '0'):
                flips += 1

        return flips