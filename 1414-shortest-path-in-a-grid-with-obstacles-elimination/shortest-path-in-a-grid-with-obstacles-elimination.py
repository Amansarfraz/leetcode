from collections import deque

class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        # If we have enough k to ignore obstacles
        if k >= m + n - 2:
            return m + n - 2

        queue = deque()
        queue.append((0, 0, 0, k))  # row, col, steps, k left

        visited = set()
        visited.add((0, 0, k))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue:
            r, c, steps, rem_k = queue.popleft()

            # reached target
            if r == m - 1 and c == n - 1:
                return steps

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    new_k = rem_k - grid[nr][nc]

                    if new_k >= 0 and (nr, nc, new_k) not in visited:
                        visited.add((nr, nc, new_k))
                        queue.append((nr, nc, steps + 1, new_k))

        return -1