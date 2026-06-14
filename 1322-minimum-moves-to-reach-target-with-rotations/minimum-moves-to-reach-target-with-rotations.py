from collections import deque

class Solution(object):
    def minimumMoves(self, grid):
        n = len(grid)

        q = deque([(0, 0, 0, 0)])  # row, col, orientation, steps
        # orientation: 0 = horizontal, 1 = vertical

        visited = {(0, 0, 0)}

        while q:
            r, c, ori, steps = q.popleft()

            if r == n - 1 and c == n - 2 and ori == 0:
                return steps

            if ori == 0:  # horizontal

                # move right
                if c + 2 < n and grid[r][c + 2] == 0:
                    state = (r, c + 1, 0)
                    if state not in visited:
                        visited.add(state)
                        q.append((r, c + 1, 0, steps + 1))

                # move down
                if r + 1 < n and grid[r + 1][c] == 0 and grid[r + 1][c + 1] == 0:
                    state = (r + 1, c, 0)
                    if state not in visited:
                        visited.add(state)
                        q.append((r + 1, c, 0, steps + 1))

                    # rotate clockwise
                    state = (r, c, 1)
                    if state not in visited:
                        visited.add(state)
                        q.append((r, c, 1, steps + 1))

            else:  # vertical

                # move down
                if r + 2 < n and grid[r + 2][c] == 0:
                    state = (r + 1, c, 1)
                    if state not in visited:
                        visited.add(state)
                        q.append((r + 1, c, 1, steps + 1))

                # move right
                if c + 1 < n and grid[r][c + 1] == 0 and grid[r + 1][c + 1] == 0:
                    state = (r, c + 1, 1)
                    if state not in visited:
                        visited.add(state)
                        q.append((r, c + 1, 1, steps + 1))

                    # rotate counter-clockwise
                    state = (r, c, 0)
                    if state not in visited:
                        visited.add(state)
                        q.append((r, c, 0, steps + 1))

        return -1