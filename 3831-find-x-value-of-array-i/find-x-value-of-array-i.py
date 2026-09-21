class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        f = [0] * k
        res = [0] * k
        for v in nums:
            g = f[:]
            f = [0] * k
            f[v % k] += 1
            for x, pre in enumerate(g):
                f[(x * v) % k] += pre
            for x in range(k):
                res[x] += f[x]
        return res

