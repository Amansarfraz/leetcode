import math

class Solution(object):
    def numPoints(self, darts, r):
        """
        :type darts: List[List[int]]
        :type r: int
        :rtype: int
        """
        n = len(darts)
        if n <= 1:
            return n

        ans = 1
        eps = 1e-7

        def count_points(cx, cy):
            cnt = 0
            for x, y in darts:
                if (x - cx) ** 2 + (y - cy) ** 2 <= r * r + eps:
                    cnt += 1
            return cnt

        for i in range(n):
            x1, y1 = darts[i]
            for j in range(i + 1, n):
                x2, y2 = darts[j]

                dx = x2 - x1
                dy = y2 - y1
                d = math.hypot(dx, dy)

                if d > 2 * r + eps:
                    continue

                mx = (x1 + x2) / 2.0
                my = (y1 + y2) / 2.0

                h = math.sqrt(max(0.0, r * r - (d / 2.0) ** 2))

                ux = -dy / d if d != 0 else 0
                uy = dx / d if d != 0 else 0

                c1x = mx + ux * h
                c1y = my + uy * h
                c2x = mx - ux * h
                c2y = my - uy * h

                ans = max(ans, count_points(c1x, c1y))
                ans = max(ans, count_points(c2x, c2y))

        return ans