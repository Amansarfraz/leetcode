class Solution(object):
    def numMagicSquaresInside(self, grid):
        
        def is_magic(x, y):
            seen = set()
            
            # check all numbers + range
            for i in range(3):
                for j in range(3):
                    val = grid[x+i][y+j]
                    if val < 1 or val > 9:
                        return False
                    seen.add(val)
            
            if len(seen) != 9:
                return False
            
            # row sums
            for i in range(3):
                if sum(grid[x+i][y:y+3]) != 15:
                    return False
            
            # column sums
            for j in range(3):
                if grid[x][y+j] + grid[x+1][y+j] + grid[x+2][y+j] != 15:
                    return False
            
            # diagonals
            if grid[x][y] + grid[x+1][y+1] + grid[x+2][y+2] != 15:
                return False
            
            if grid[x][y+2] + grid[x+1][y+1] + grid[x+2][y] != 15:
                return False
            
            return True
        
        n, m = len(grid), len(grid[0])
        count = 0
        
        for i in range(n - 2):
            for j in range(m - 2):
                if is_magic(i, j):
                    count += 1
        
        return count