from collections import deque

class Solution(object):
    def minFlips(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])

        start = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    start |= (1 << (i * n + j))

        if start == 0:
            return 0

        masks = []
        dirs = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(m):
            for j in range(n):
                mask = 0
                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n:
                        mask ^= (1 << (ni * n + nj))
                masks.append(mask)

        q = deque([(start, 0)])
        visited = {start}

        while q:
            state, steps = q.popleft()

            if state == 0:
                return steps

            for mask in masks:
                nxt = state ^ mask
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, steps + 1))

        return -1