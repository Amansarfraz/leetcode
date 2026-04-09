class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        MOD = 10**9 + 7

        memo = {}

        def dfs(r, c, moves):
            # out of boundary → valid path
            if r < 0 or r >= m or c < 0 or c >= n:
                return 1

            # no moves left
            if moves == 0:
                return 0

            if (r, c, moves) in memo:
                return memo[(r, c, moves)]

            res = (
                dfs(r + 1, c, moves - 1) +
                dfs(r - 1, c, moves - 1) +
                dfs(r, c + 1, moves - 1) +
                dfs(r, c - 1, moves - 1)
            )

            memo[(r, c, moves)] = res % MOD
            return memo[(r, c, moves)]

        return dfs(startRow, startColumn, maxMove)