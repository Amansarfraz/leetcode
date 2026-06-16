class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        m, n = len(mat), len(mat[0])

        # Prefix sum
        pref = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                pref[i + 1][j + 1] = (
                    mat[i][j]
                    + pref[i][j + 1]
                    + pref[i + 1][j]
                    - pref[i][j]
                )

        def can(k):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    total = (
                        pref[i + k][j + k]
                        - pref[i][j + k]
                        - pref[i + k][j]
                        + pref[i][j]
                    )
                    if total <= threshold:
                        return True
            return False

        left, right = 0, min(m, n)

        while left < right:
            mid = (left + right + 1) // 2

            if can(mid):
                left = mid
            else:
                right = mid - 1

        return left