class Solution(object):
    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}

        def dfs(x):
            if x <= 1:
                return x
            if x in memo:
                return memo[x]

            memo[x] = 1 + min(
                x % 2 + dfs(x // 2),
                x % 3 + dfs(x // 3)
            )
            return memo[x]

        return dfs(n)