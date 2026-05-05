class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        result = []
        
        # directions: right, down, left, up
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        
        steps = 1
        r, c = rStart, cStart
        
        result.append([r, c])
        
        while len(result) < rows * cols:
            for i in range(4):
                dr, dc = dirs[i]
                
                # increase step after every 2 directions
                for _ in range(steps):
                    r += dr
                    c += dc
                    
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                
                if i % 2 == 1:
                    steps += 1
        
        return result