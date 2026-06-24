from collections import deque

class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0

        dq = deque([(0, 0)])

        while dq:
            r, c = dq.popleft()

            for k, (dr, dc) in enumerate(dirs, start=1):
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    cost = dist[r][c] + (0 if grid[r][c] == k else 1)

                    if cost < dist[nr][nc]:
                        dist[nr][nc] = cost

                        if grid[r][c] == k:
                            dq.appendleft((nr, nc))
                        else:
                            dq.append((nr, nc))

        return dist[m - 1][n - 1]