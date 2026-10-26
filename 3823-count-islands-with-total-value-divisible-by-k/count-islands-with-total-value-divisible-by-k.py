class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island_count = 0
        
        def dfs(r, c):
            # Base cases: out of bounds or water cell (value <= 0)
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] <= 0:
                return 0
            
            # Save current cell value and sink it to mark as visited
            current_value = grid[r][c]
            grid[r][c] = 0 
            
            # Traverse all 4 cardinal directions and accumulate the values
            total_sum = current_value
            total_sum += dfs(r + 1, c)
            total_sum += dfs(r - 1, c)
            total_sum += dfs(r, c + 1)
            total_sum += dfs(r, c - 1)
            
            return total_sum

        # Traverse every cell in the grid to find unvisited land
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    # Run DFS to calculate the full sum of this island
                    island_sum = dfs(r, c)
                    # Check if the total island value is divisible by k
                    if island_sum % k == 0:
                        island_count += 1
                    
        return island_count
