class Solution(object):
    def palindromePartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)

        # Step 1: cost[i][j]
        cost = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    cost[i][j] = cost[i + 1][j - 1] if i + 1 <= j - 1 else 0
                else:
                    cost[i][j] = (cost[i + 1][j - 1] if i + 1 <= j - 1 else 0) + 1

        INF = float('inf')
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        # Step 2: DP transitions
        for p in range(1, k + 1):
            for i in range(1, n + 1):
                if p == 1:
                    dp[p][i] = cost[0][i - 1]
                else:
                    for j in range(p - 1, i):
                        dp[p][i] = min(dp[p][i], dp[p - 1][j] + cost[j][i - 1])

        return dp[k][n]