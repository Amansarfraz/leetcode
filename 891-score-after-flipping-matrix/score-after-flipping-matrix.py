class Solution(object):
    def matrixScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0])

        # Step 1: Make first column all 1s (flip rows if needed)
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1  # flip bit

        # Step 2: Maximize each column
        for j in range(1, n):
            zeros = 0
            ones = 0

            for i in range(m):
                if grid[i][j] == 0:
                    zeros += 1
                else:
                    ones += 1

            # flip column if zeros are more
            if zeros > ones:
                for i in range(m):
                    grid[i][j] ^= 1

        # Step 3: Calculate score
        result = 0
        for i in range(m):
            value = 0
            for j in range(n):
                value = value * 2 + grid[i][j]
            result += value

        return result