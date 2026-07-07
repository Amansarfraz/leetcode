class Solution(object):
    def minCost(self, houses, cost, m, n, target):
        """
        :type houses: List[int]
        :type cost: List[List[int]]
        :type m: int
        :type n: int
        :type target: int
        :rtype: int
        """
        INF = float('inf')
        memo = {}

        def dfs(i, prev, groups):
            if groups > target:
                return INF

            if i == m:
                return 0 if groups == target else INF

            key = (i, prev, groups)
            if key in memo:
                return memo[key]

            if houses[i] != 0:
                ans = dfs(i + 1, houses[i], groups + (houses[i] != prev))
            else:
                ans = INF
                for color in range(1, n + 1):
                    ans = min(
                        ans,
                        cost[i][color - 1] +
                        dfs(i + 1, color, groups + (color != prev))
                    )

            memo[key] = ans
            return ans

        res = dfs(0, 0, 0)
        return -1 if res == INF else res