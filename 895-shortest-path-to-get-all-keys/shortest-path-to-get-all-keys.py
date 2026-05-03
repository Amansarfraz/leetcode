from collections import deque

class Solution(object):
    def shortestPathAllKeys(self, grid):
        m, n = len(grid), len(grid[0])
        
        # Find start and count keys
        total_keys = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start = (i, j)
                elif 'a' <= grid[i][j] <= 'f':
                    total_keys = max(total_keys, ord(grid[i][j]) - ord('a') + 1)
        
        # Final mask when all keys collected
        final_mask = (1 << total_keys) - 1
        
        # BFS queue: (row, col, keys_mask, steps)
        q = deque([(start[0], start[1], 0, 0)])
        
        # Visited: (row, col, keys_mask)
        visited = set([(start[0], start[1], 0)])
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while q:
            x, y, keys, steps = q.popleft()
            
            # If all keys collected
            if keys == final_mask:
                return steps
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n:
                    cell = grid[nx][ny]
                    
                    # Wall
                    if cell == '#':
                        continue
                    
                    new_keys = keys
                    
                    # Key
                    if 'a' <= cell <= 'f':
                        new_keys |= (1 << (ord(cell) - ord('a')))
                    
                    # Lock
                    if 'A' <= cell <= 'F':
                        if not (keys & (1 << (ord(cell) - ord('A')))):
                            continue
                    
                    state = (nx, ny, new_keys)
                    
                    if state not in visited:
                        visited.add(state)
                        q.append((nx, ny, new_keys, steps + 1))
        
        return -1