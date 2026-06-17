from collections import deque

class Solution(object):
    def minPushBox(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    sx, sy = i, j
                elif grid[i][j] == 'B':
                    bx, by = i, j
                elif grid[i][j] == 'T':
                    tx, ty = i, j

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        dq = deque([(0, bx, by, sx, sy)])
        visited = set([(bx, by, sx, sy)])

        while dq:
            pushes, bx, by, px, py = dq.popleft()

            if (bx, by) == (tx, ty):
                return pushes

            for dx, dy in dirs:
                npx, npy = px + dx, py + dy

                if not (0 <= npx < m and 0 <= npy < n):
                    continue
                if grid[npx][npy] == '#':
                    continue

                if (npx, npy) == (bx, by):
                    nbx, nby = bx + dx, by + dy

                    if not (0 <= nbx < m and 0 <= nby < n):
                        continue
                    if grid[nbx][nby] == '#':
                        continue

                    state = (nbx, nby, npx, npy)
                    if state not in visited:
                        visited.add(state)
                        dq.append((pushes + 1, nbx, nby, npx, npy))
                else:
                    state = (bx, by, npx, npy)
                    if state not in visited:
                        visited.add(state)
                        dq.appendleft((pushes, bx, by, npx, npy))

        return -1