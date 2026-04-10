class Solution(object):
    def validSquare(self, p1, p2, p3, p4):

        def dist(a, b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

        points = [p1, p2, p3, p4]
        d = []

        # all pair distances (6 total)
        for i in range(4):
            for j in range(i + 1, 4):
                d.append(dist(points[i], points[j]))

        d.sort()

        # 0 distance means overlapping points → invalid
        if d[0] == 0:
            return False

        # 4 sides must be equal + 2 diagonals must be equal
        return (
            d[0] == d[1] == d[2] == d[3] and
            d[4] == d[5] and
            d[4] > d[0]
        )