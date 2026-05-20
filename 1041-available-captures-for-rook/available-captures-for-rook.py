class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        rows, cols = 8, 8

        # Find the rook position
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'R':
                    r, c = i, j

        captures = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dr, dc in directions:
            x, y = r + dr, c + dc

            while 0 <= x < rows and 0 <= y < cols:
                if board[x][y] == 'B':
                    break

                if board[x][y] == 'p':
                    captures += 1
                    break

                x += dr
                y += dc

        return captures