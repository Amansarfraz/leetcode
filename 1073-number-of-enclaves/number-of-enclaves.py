class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        rows = len(grid)
        cols = len(grid[0])
        
        # DFS to remove boundary-connected land
        def dfs(r, c):
            
            # Out of bounds or water
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return
            
            # Mark visited
            grid[r][c] = 0
            
            # Explore 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        
        # Remove lands connected to borders
        
        # First and last column
        for r in range(rows):
            if grid[r][0] == 1:
                dfs(r, 0)
            
            if grid[r][cols - 1] == 1:
                dfs(r, cols - 1)
        
        
        # First and last row
        for c in range(cols):
            if grid[0][c] == 1:
                dfs(0, c)
            
            if grid[rows - 1][c] == 1:
                dfs(rows - 1, c)
        
        
        # Count remaining land cells
        count = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    count += 1
        
        return count