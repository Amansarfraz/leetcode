class Solution(object):
    def swimInWater(self, grid):
        import heapq
        
        n = len(grid)
        visited = set()
        
        # (time, row, col)
        heap = [(grid[0][0], 0, 0)]
        visited.add((0, 0))
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while heap:
            time, r, c = heapq.heappop(heap)
            
            if r == n - 1 and c == n - 1:
                return time
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(heap, (max(time, grid[nr][nc]), nr, nc))