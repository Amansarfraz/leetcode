class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        count = {}
        ans = 0

        for a, b in dominoes:
            key = (min(a, b), max(a, b))

            ans += count.get(key, 0)
            count[key] = count.get(key, 0) + 1

        return ans