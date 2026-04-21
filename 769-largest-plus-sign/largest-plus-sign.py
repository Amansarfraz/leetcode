class Solution(object):
    def orderOfLargestPlusSign(self, n, mines):
        grid = [[n] * n for _ in range(n)]
        
        # mark mines
        for r, c in mines:
            grid[r][c] = 0
        
        # left & right
        for i in range(n):
            count = 0
            for j in range(n):
                count = 0 if grid[i][j] == 0 else count + 1
                grid[i][j] = min(grid[i][j], count)
            
            count = 0
            for j in range(n-1, -1, -1):
                count = 0 if grid[i][j] == 0 else count + 1
                grid[i][j] = min(grid[i][j], count)
        
        # up & down
        for j in range(n):
            count = 0
            for i in range(n):
                count = 0 if grid[i][j] == 0 else count + 1
                grid[i][j] = min(grid[i][j], count)
            
            count = 0
            for i in range(n-1, -1, -1):
                count = 0 if grid[i][j] == 0 else count + 1
                grid[i][j] = min(grid[i][j], count)
        
        # find max
        res = 0
        for i in range(n):
            for j in range(n):
                res = max(res, grid[i][j])
        
        return res