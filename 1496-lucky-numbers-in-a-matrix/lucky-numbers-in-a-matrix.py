class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row_min = [min(row) for row in matrix]
        col_max = [max(col) for col in zip(*matrix)]

        ans = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == row_min[i] and matrix[i][j] == col_max[j]:
                    ans.append(matrix[i][j])

        return ans