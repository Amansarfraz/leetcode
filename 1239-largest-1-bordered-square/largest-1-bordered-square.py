class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        right = [[0] * n for _ in range(m)]
        down = [[0] * n for _ in range(m)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    right[i][j] = 1 + (right[i][j + 1] if j + 1 < n else 0)
                    down[i][j] = 1 + (down[i + 1][j] if i + 1 < m else 0)

        for size in range(min(m, n), 0, -1):
            for i in range(m - size + 1):
                for j in range(n - size + 1):
                    if (right[i][j] >= size and
                        down[i][j] >= size and
                        right[i + size - 1][j] >= size and
                        down[i][j + size - 1] >= size):
                        return size * size

        return 0