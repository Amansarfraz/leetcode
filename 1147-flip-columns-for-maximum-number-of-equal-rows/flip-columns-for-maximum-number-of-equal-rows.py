class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        count = {}

        for row in matrix:
            if row[0] == 1:
                pattern = tuple(1 - x for x in row)
            else:
                pattern = tuple(row)

            count[pattern] = count.get(pattern, 0) + 1

        return max(count.values())