class Solution(object):
    def connectTwoGroups(self, cost):
        """
        :type cost: List[List[int]]
        :rtype: int
        """
        m, n = len(cost), len(cost[0])

        minCost = [min(cost[i][j] for i in range(m)) for j in range(n)]
        memo = {}

        def dfs(i, mask):
            if (i, mask) in memo:
                return memo[(i, mask)]

            if i == m:
                ans = 0
                for j in range(n):
                    if (mask & (1 << j)) == 0:
                        ans += minCost[j]
                return ans

            res = float('inf')
            for j in range(n):
                res = min(res, cost[i][j] + dfs(i + 1, mask | (1 << j)))

            memo[(i, mask)] = res
            return res

        return dfs(0, 0)