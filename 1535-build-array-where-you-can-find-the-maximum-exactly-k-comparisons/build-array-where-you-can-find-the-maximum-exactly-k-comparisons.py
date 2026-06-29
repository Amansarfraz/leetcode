class Solution(object):
    def numOfArrays(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7

        dp = [[[0] * (m + 1) for _ in range(k + 1)] for _ in range(n + 1)]

        for maxVal in range(1, m + 1):
            dp[1][1][maxVal] = 1

        for length in range(2, n + 1):
            for cost in range(1, k + 1):
                prefix = 0
                for maxVal in range(1, m + 1):
                    # New maximum
                    prefix = (prefix + dp[length - 1][cost - 1][maxVal - 1]) % MOD

                    # Keep current maximum
                    dp[length][cost][maxVal] = (
                        dp[length - 1][cost][maxVal] * maxVal + prefix
                    ) % MOD

        ans = 0
        for maxVal in range(1, m + 1):
            ans = (ans + dp[n][k][maxVal]) % MOD

        return ans