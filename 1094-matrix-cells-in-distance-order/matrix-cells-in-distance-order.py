class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """

        result = []

        for r in range(rows):
            for c in range(cols):
                dist = abs(r - rCenter) + abs(c - cCenter)
                result.append([dist, r, c])

        result.sort()

        return [[r, c] for dist, r, c in result]