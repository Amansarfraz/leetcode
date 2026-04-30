class Solution(object):
    def largestIsland(self, grid):
        n = len(grid)
        island_size = {}
        island_id = 2
        
        def dfs(r, c, id):
            if r < 0 or c < 0 or r >= n or c >= n or grid[r][c] != 1:
                return 0
            
            grid[r][c] = id
            size = 1
            
            size += dfs(r+1, c, id)
            size += dfs(r-1, c, id)
            size += dfs(r, c+1, id)
            size += dfs(r, c-1, id)
            
            return size
        
        # Step 1: label islands
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_size[island_id] = dfs(i, j, island_id)
                    island_id += 1
        
        # Step 2: try flipping 0
        res = max(island_size.values() or [0])
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    size = 1
                    
                    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                        x, y = i + dx, j + dy
                        if 0 <= x < n and 0 <= y < n:
                            id = grid[x][y]
                            if id > 1 and id not in seen:
                                size += island_size[id]
                                seen.add(id)
                    
                    res = max(res, size)
        
        return res