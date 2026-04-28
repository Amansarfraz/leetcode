class Solution(object):
    def hitBricks(self, grid, hits):
        m, n = len(grid), len(grid[0])
        
        parent = {}
        size = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            parent[ry] = rx
            size[rx] += size[ry]
        
        def index(r, c):
            return r * n + c
        
        top = m * n  # virtual top node
        
        # Step 1: copy grid and remove hits
        copy = [row[:] for row in grid]
        for r, c in hits:
            if copy[r][c] == 1:
                copy[r][c] = 0
        
        # Initialize DSU
        for r in range(m):
            for c in range(n):
                if copy[r][c] == 1:
                    idx = index(r, c)
                    parent[idx] = idx
                    size[idx] = 1
        
        parent[top] = top
        size[top] = 1
        
        # Connect initial grid
        for r in range(m):
            for c in range(n):
                if copy[r][c] == 1:
                    idx = index(r, c)
                    
                    if r == 0:
                        union(idx, top)
                    
                    for dr, dc in [(1,0),(0,1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n and copy[nr][nc] == 1:
                            union(idx, index(nr, nc))
        
        def getTopSize():
            return size[find(top)]
        
        res = []
        
        # Step 2: process hits in reverse
        for r, c in reversed(hits):
            if grid[r][c] == 0:
                res.append(0)
                continue
            
            before = getTopSize()
            
            idx = index(r, c)
            parent[idx] = idx
            size[idx] = 1
            
            if r == 0:
                union(idx, top)
            
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and copy[nr][nc] == 1:
                    union(idx, index(nr, nc))
            
            copy[r][c] = 1
            
            after = getTopSize()
            
            fallen = max(0, after - before - 1)
            res.append(fallen)
        
        return res[::-1]