class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0

            gold = grid[r][c]
            grid[r][c] = 0

            best = max(
                dfs(r + 1, c),
                dfs(r - 1, c),
                dfs(r, c + 1),
                dfs(r, c - 1)
            )

            grid[r][c] = gold
            return gold + best

        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    ans = max(ans, dfs(i, j))

        return ans