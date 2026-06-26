class Solution(object):
    def maxSizeSlices(self, slices):
        """
        :type slices: List[int]
        :rtype: int
        """
        def solve(arr):
            m = len(arr)
            choose = len(slices) // 3

            dp = [[0] * (choose + 1) for _ in range(m + 2)]

            for i in range(m - 1, -1, -1):
                for j in range(1, choose + 1):
                    take = arr[i] + dp[i + 2][j - 1]
                    skip = dp[i + 1][j]
                    dp[i][j] = max(take, skip)

            return dp[0][choose]

        return max(solve(slices[:-1]), solve(slices[1:]))