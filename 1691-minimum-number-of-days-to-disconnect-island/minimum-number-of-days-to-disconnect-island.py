class Solution(object):
    def minDays(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        def count_islands():
            visited = [[False] * cols for _ in range(rows)]

            def dfs(r, c):
                if (r < 0 or r >= rows or c < 0 or c >= cols or
                    visited[r][c] or grid[r][c] == 0):
                    return
                visited[r][c] = True
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

            islands = 0
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1 and not visited[i][j]:
                        islands += 1
                        dfs(i, j)
            return islands

        if count_islands() != 1:
            return 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands() != 1:
                        grid[i][j] = 1
                        return 1
                    grid[i][j] = 1

        return 2