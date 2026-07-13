import math

class Solution(object):
    def getMinDistSum(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: float
        """
        x = sum(p[0] for p in positions) / float(len(positions))
        y = sum(p[1] for p in positions) / float(len(positions))

        def dist_sum(x, y):
            return sum(math.hypot(x - px, y - py) for px, py in positions)

        step = 100.0
        ans = dist_sum(x, y)

        while step > 1e-6:
            improved = False

            for dx, dy in [(step, 0), (-step, 0), (0, step), (0, -step)]:
                nx, ny = x + dx, y + dy
                d = dist_sum(nx, ny)

                if d < ans:
                    ans = d
                    x, y = nx, ny
                    improved = True
                    break

            if not improved:
                step *= 0.5

        return ans

        