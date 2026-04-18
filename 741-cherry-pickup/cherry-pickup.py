class Solution(object):
    def cherryPickup(self, grid):
        n = len(grid)
        memo = {}

        def dp(r1, c1, r2):
            c2 = r1 + c1 - r2

            # out of bounds or thorn
            if (r1 >= n or c1 >= n or 
                r2 >= n or c2 >= n or
                grid[r1][c1] == -1 or grid[r2][c2] == -1):
                return float('-inf')

            # reached end
            if r1 == n-1 and c1 == n-1:
                return grid[r1][c1]

            if (r1, c1, r2) in memo:
                return memo[(r1, c1, r2)]

            cherries = grid[r1][c1]

            # avoid double count
            if (r1, c1) != (r2, c2):
                cherries += grid[r2][c2]

            # explore all 4 moves
            best = max(
                dp(r1+1, c1, r2+1),   # down, down
                dp(r1, c1+1, r2),     # right, right
                dp(r1+1, c1, r2),     # down, right
                dp(r1, c1+1, r2+1)    # right, down
            )

            cherries += best
            memo[(r1, c1, r2)] = cherries
            return cherries

        result = dp(0, 0, 0)
        return max(0, result)