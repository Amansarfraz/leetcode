class Solution(object):
    def containVirus(self, isInfected):
        m, n = len(isInfected), len(isInfected[0])
        total_walls = 0
        
        def dfs(r, c, visited, region, frontier):
            stack = [(r, c)]
            walls = 0
            
            while stack:
                x, y = stack.pop()
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                region.append((x, y))
                
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx, ny = x + dx, y + dy
                    
                    if 0 <= nx < m and 0 <= ny < n:
                        if isInfected[nx][ny] == 1 and (nx, ny) not in visited:
                            stack.append((nx, ny))
                        elif isInfected[nx][ny] == 0:
                            frontier.add((nx, ny))
                            walls += 1
            return walls
        
        while True:
            visited = set()
            regions = []
            frontiers = []
            walls_needed = []
            
            # Step 1: find all regions
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and (i, j) not in visited:
                        region = []
                        frontier = set()
                        walls = dfs(i, j, visited, region, frontier)
                        
                        regions.append(region)
                        frontiers.append(frontier)
                        walls_needed.append(walls)
            
            if not regions:
                break
            
            # Step 2: pick region with max spread
            idx = 0
            for i in range(len(frontiers)):
                if len(frontiers[i]) > len(frontiers[idx]):
                    idx = i
            
            # Step 3: add walls
            total_walls += walls_needed[idx]
            
            # Step 4: quarantine that region
            for r, c in regions[idx]:
                isInfected[r][c] = -1  # blocked
            
            # Step 5: spread other regions
            for i in range(len(regions)):
                if i == idx:
                    continue
                for r, c in frontiers[i]:
                    isInfected[r][c] = 1
            
            # stop if no spread possible
            if all(len(frontiers[i]) == 0 for i in range(len(frontiers))):
                break
        
        return total_walls