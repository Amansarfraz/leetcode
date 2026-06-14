class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """

        queen_set = set(map(tuple, queens))

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        res = []

        for dx, dy in directions:
            x, y = king[0], king[1]

            while 0 <= x < 8 and 0 <= y < 8:
                if (x, y) in queen_set:
                    res.append([x, y])
                    break
                x += dx
                y += dy

        return res