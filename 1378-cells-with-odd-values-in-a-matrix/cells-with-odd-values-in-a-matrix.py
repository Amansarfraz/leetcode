class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        rows = [0] * m
        cols = [0] * n

        for r, c in indices:
            rows[r] ^= 1
            cols[c] ^= 1

        odd_rows = sum(rows)
        odd_cols = sum(cols)

        return odd_rows * (n - odd_cols) + (m - odd_rows) * odd_cols