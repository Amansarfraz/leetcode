class Solution(object):
    def tilingRectangle(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if n > m:
            n, m = m, n

        self.ans = n * m
        heights = [0] * m

        def dfs(cnt):
            if cnt >= self.ans:
                return

            h = min(heights)
            if h == n:
                self.ans = min(self.ans, cnt)
                return

            idx = heights.index(h)

            max_size = 1
            while (idx + max_size <= m and
                   all(heights[idx + k] == h for k in range(max_size)) and
                   h + max_size <= n):
                max_size += 1

            for size in range(max_size - 1, 0, -1):
                for k in range(size):
                    heights[idx + k] += size

                dfs(cnt + 1)

                for k in range(size):
                    heights[idx + k] -= size

        dfs(0)
        return self.ans