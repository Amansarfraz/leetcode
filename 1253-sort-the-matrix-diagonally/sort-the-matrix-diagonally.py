class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict

        m, n = len(mat), len(mat[0])
        diag = defaultdict(list)

        # Step 1: collect diagonals
        for i in range(m):
            for j in range(n):
                diag[i - j].append(mat[i][j])

        # Step 2: sort each diagonal
        for key in diag:
            diag[key].sort(reverse=True)  # reverse for efficient pop()

        # Step 3: put back into matrix
        for i in range(m):
            for j in range(n):
                mat[i][j] = diag[i - j].pop()

        return mat