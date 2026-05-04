class Solution(object):
    def profitableSchemes(self, n, minProfit, group, profit):
        """
        :type n: int
        :type minProfit: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """

        MOD = 10**9 + 7
        m = len(group)

        # dp[i][j] = ways using i people to get j profit
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for k in range(m):
            g = group[k]
            p = profit[k]

            # reverse loop (important for 0/1 knapsack)
            for i in range(n, g - 1, -1):
                for j in range(minProfit, -1, -1):

                    new_profit = min(minProfit, j + p)

                    dp[i][new_profit] = (dp[i][new_profit] + dp[i - g][j]) % MOD

        # sum all ways with profit >= minProfit
        return sum(dp[i][minProfit] for i in range(n + 1)) % MOD