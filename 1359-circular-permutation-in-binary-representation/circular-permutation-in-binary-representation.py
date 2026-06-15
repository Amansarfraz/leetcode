class Solution(object):
    def circularPermutation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: List[int]
        """
        gray = [i ^ (i >> 1) for i in range(1 << n)]

        idx = gray.index(start)

        return gray[idx:] + gray[:idx]