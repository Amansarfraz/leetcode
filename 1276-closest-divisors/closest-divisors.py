class Solution(object):
    def closestDivisors(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        import math

        def findPair(x):
            d = int(math.sqrt(x))
            while d > 0:
                if x % d == 0:
                    return [d, x // d]
                d -= 1

        p1 = findPair(num + 1)
        p2 = findPair(num + 2)

        if abs(p1[0] - p1[1]) < abs(p2[0] - p2[1]):
            return p1
        return p2