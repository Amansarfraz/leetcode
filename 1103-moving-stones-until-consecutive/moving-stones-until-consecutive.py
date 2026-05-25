class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """

        stones = sorted([a, b, c])

        x, y, z = stones

        # Maximum moves
        max_moves = (z - x) - 2

        # Minimum moves
        if z - x == 2:
            min_moves = 0
        elif y - x <= 2 or z - y <= 2:
            min_moves = 1
        else:
            min_moves = 2

        return [min_moves, max_moves]