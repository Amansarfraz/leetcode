class Solution(object):
    def minDistance(self, houses, k):
        """
        :type houses: List[int]
        :type k: int
        :rtype: int
        """
        houses.sort()
        n = len(houses)

        # cost[i][j] = minimum distance for houses[i...j] using one mailbox
        cost = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i, n):
                m = (i + j) // 2
                for t in range(i, j + 1):
                    cost[i][j] += abs(houses[t] - houses[m])

        memo = {}

        def dp(i, k):
            if i == n and k == 0:
                return 0
            if i == n or k == 0:
                return float('inf')

            if (i, k) in memo:
                return memo[(i, k)]

            res = float('inf')

            for j in range(i, n):
                res = min(res, cost[i][j] + dp(j + 1, k - 1))

            memo[(i, k)] = res
            return res

        return dp(0, k)