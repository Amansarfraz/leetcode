class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        n = len(grid)
        size = n * 3
        
        expanded = [[0] * size for _ in range(size)]

        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    expanded[i * 3][j * 3 + 2] = 1
                    expanded[i * 3 + 1][j * 3 + 1] = 1
                    expanded[i * 3 + 2][j * 3] = 1

                elif grid[i][j] == '\\':
                    expanded[i * 3][j * 3] = 1
                    expanded[i * 3 + 1][j * 3 + 1] = 1
                    expanded[i * 3 + 2][j * 3 + 2] = 1

        def dfs(r, c):
            if r < 0 or c < 0 or r >= size or c >= size or expanded[r][c] != 0:
                return

            expanded[r][c] = 2

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        regions = 0

        for i in range(size):
            for j in range(size):
                if expanded[i][j] == 0:
                    dfs(i, j)
                    regions += 1

        return regions