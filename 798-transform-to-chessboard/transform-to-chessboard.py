class Solution(object):
    def movesToChessboard(self, board):
        n = len(board)
        
        # check valid transformation
        def check(lines):
            first = lines[0]
            inv = [1 - x for x in first]
            
            count_first = 0
            for row in lines:
                if row == first:
                    count_first += 1
                elif row != inv:
                    return False
            return True
        
        # convert rows/cols to tuples
        rows = [tuple(r) for r in board]
        cols = [tuple(board[i][j] for i in range(n)) for j in range(n)]
        
        # validate structure
        def valid(lines):
            first = lines[0]
            inv = tuple(1 - x for x in first)
            
            c1 = c2 = 0
            for line in lines:
                if line == first:
                    c1 += 1
                elif line == inv:
                    c2 += 1
                else:
                    return False
            
            return abs(c1 - c2) <= 1
        
        if not valid(rows) or not valid(cols):
            return -1
        
        # compute swaps
        def min_swaps(line):
            ones = sum(line)
            n = len(line)
            
            if n % 2:
                if ones * 2 < n:
                    pattern = [0,1]* (n//2) + [0]
                else:
                    pattern = [1,0]* (n//2) + [1]
            else:
                pattern1 = [0,1] * (n//2)
                pattern2 = [1,0] * (n//2)
                
                diff1 = sum(line[i] != pattern1[i] for i in range(n))
                diff2 = sum(line[i] != pattern2[i] for i in range(n))
                
                return min(diff1, diff2) // 2
            
            return sum(line[i] != pattern[i] for i in range(n)) // 2
        
        row_swaps = min_swaps([x for x in board[0]])
        col_swaps = min_swaps([board[i][0] for i in range(n)])
        
        return row_swaps + col_swaps