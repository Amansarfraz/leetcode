class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        n = len(grid)
        
        row_max = [max(row) for row in grid]
        col_max = [max(grid[i][j] for i in range(n)) for j in range(n)]
        
        total_increase = 0
        
        for i in range(n):
            for j in range(n):
                allowed = min(row_max[i], col_max[j])
                total_increase += (allowed - grid[i][j])
        
        return total_increase