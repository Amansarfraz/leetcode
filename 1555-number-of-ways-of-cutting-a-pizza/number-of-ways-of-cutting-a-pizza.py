class Solution(object):
    def ways(self, pizza, k):
        MOD = 10 ** 9 + 7
        m, n = len(pizza), len(pizza[0])

        apples = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                apples[i][j] = apples[i + 1][j] + apples[i][j + 1] - apples[i + 1][j + 1] + (pizza[i][j] == 'A')

        memo = {}

        def dfs(r, c, cuts):
            if (r, c, cuts) in memo:
                return memo[(r, c, cuts)]

            if apples[r][c] == 0:
                return 0

            if cuts == 1:
                return 1

            ans = 0

            for nr in range(r + 1, m):
                if apples[r][c] > apples[nr][c]:
                    ans = (ans + dfs(nr, c, cuts - 1)) % MOD

            for nc in range(c + 1, n):
                if apples[r][c] > apples[r][nc]:
                    ans = (ans + dfs(r, nc, cuts - 1)) % MOD

            memo[(r, c, cuts)] = ans
            return ans

        return dfs(0, 0, k)