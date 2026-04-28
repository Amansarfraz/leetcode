class Solution(object):
    def validTicTacToe(self, board):
        
        # Count X and O
        x_count = sum(row.count('X') for row in board)
        o_count = sum(row.count('O') for row in board)
        
        # Rule 1: move count valid
        if not (x_count == o_count or x_count == o_count + 1):
            return False
        
        # Helper to check win
        def win(player):
            # Rows
            for i in range(3):
                if all(board[i][j] == player for j in range(3)):
                    return True
            # Columns
            for j in range(3):
                if all(board[i][j] == player for i in range(3)):
                    return True
            # Diagonals
            if all(board[i][i] == player for i in range(3)):
                return True
            if all(board[i][2-i] == player for i in range(3)):
                return True
            
            return False
        
        x_win = win('X')
        o_win = win('O')
        
        # Rule 2 & 3
        if x_win and o_win:
            return False
        if x_win and x_count != o_count + 1:
            return False
        if o_win and x_count != o_count:
            return False
        
        return True