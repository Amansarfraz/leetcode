class Solution(object):
    def surfaceArea(self, grid):
        n = len(grid)
        area = 0
        
        for i in range(n):
            for j in range(n):
                h = grid[i][j]
                
                if h > 0:
                    # top + bottom + all 4 sides
                    area += 2 + 4 * h
                
                # subtract overlap with top cell
                if i > 0:
                    area -= 2 * min(h, grid[i-1][j])
                
                # subtract overlap with left cell
                if j > 0:
                    area -= 2 * min(h, grid[i][j-1])
        
        return area