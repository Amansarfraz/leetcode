from collections import deque

class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        n = len(grid)
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        queue = deque()
        
        # DFS to find first island
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= n or c >= n or 
                grid[r][c] != 1):
                return
            
            grid[r][c] = 2
            queue.append((r, c))
            
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        found = False
        
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break
        
        # BFS to reach second island
        steps = 0
        
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < n and 0 <= nc < n:
                        if grid[nr][nc] == 1:
                            return steps
                        
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 2
                            queue.append((nr, nc))
            
            steps += 1