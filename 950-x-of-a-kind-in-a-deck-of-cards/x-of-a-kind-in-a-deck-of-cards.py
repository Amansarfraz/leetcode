from collections import Counter

class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        count = Counter(deck)

        g = 0
        for v in count.values():
            g = self.gcd(g, v)

        return g >= 2