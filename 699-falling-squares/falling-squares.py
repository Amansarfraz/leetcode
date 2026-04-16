class Solution(object):
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """

        squares = []  # store (left, right, height)
        result = []
        max_height = 0

        for left, size in positions:
            right = left + size
            height = size

            base = 0

            for l, r, h in squares:
                # check overlap
                if not (r <= left or l >= right):
                    base = max(base, h)

            new_height = base + height
            squares.append((left, right, new_height))

            max_height = max(max_height, new_height)
            result.append(max_height)

        return result