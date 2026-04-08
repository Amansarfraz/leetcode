class Solution(object):
    def updateBoard(self, board, click):
        m, n = len(board), len(board[0])
        x, y = click
        
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        
        def dfs(i, j):
            if board[i][j] != 'E':
                return
            
            # Count adjacent mines
            mines = 0
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'M':
                        mines += 1
            
            if mines > 0:
                board[i][j] = str(mines)
            else:
                board[i][j] = 'B'
                for dx in [-1,0,1]:
                    for dy in [-1,0,1]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < m and 0 <= nj < n:
                            dfs(ni, nj)
        
        dfs(x, y)
        return board