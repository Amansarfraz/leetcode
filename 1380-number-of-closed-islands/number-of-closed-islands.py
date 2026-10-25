class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            # Base case: if out of bounds or water, stop
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 1:
                return
            # Mark the cell as visited by turning it into water
            grid[r][c] = 1
            # Flood fill in all 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1: Remove all land connected to the boundaries
        for r in range(rows):
            for c in range(cols):
                # Check if it's on the boundary
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    if grid[r][c] == 0:
                        dfs(r, c)
                        
        # Step 2: Count the remaining isolated closed islands
        closed_islands = 0
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if grid[r][c] == 0:
                    closed_islands += 1
                    dfs(r, c) # Flood fill to sink the rest of this island
                    
        return closed_islands
