from collections import deque

class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        if not mat or not mat[0]:
            return mat
        
        m, n = len(mat), len(mat[0])
        res = [[-1]*n for _ in range(m)]  # Initialize distances as -1
        queue = deque()
        
        # Start BFS from all 0s
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    queue.append((i, j))
        
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and res[nx][ny] == -1:
                    res[nx][ny] = res[x][y] + 1
                    queue.append((nx, ny))
        
        return res