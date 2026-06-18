class Solution(object):
    def minFallingPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)

        dp = grid[0][:]

        for i in range(1, n):
            min1 = min2 = float('inf')
            idx1 = -1

            for j in range(n):
                if dp[j] < min1:
                    min2 = min1
                    min1 = dp[j]
                    idx1 = j
                elif dp[j] < min2:
                    min2 = dp[j]

            new_dp = [0] * n

            for j in range(n):
                if j == idx1:
                    new_dp[j] = grid[i][j] + min2
                else:
                    new_dp[j] = grid[i][j] + min1

            dp = new_dp

        return min(dp)