class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat)
        total = 0

        for i in range(n):
            total += mat[i][i]          # Primary diagonal
            total += mat[i][n - 1 - i]  # Secondary diagonal

        # Agar matrix odd size ki hai to center element do baar add hua hoga
        if n % 2 == 1:
            total -= mat[n // 2][n // 2]

        return total