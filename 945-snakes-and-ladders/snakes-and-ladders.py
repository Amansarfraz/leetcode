from collections import deque

class Solution(object):
    def snakesAndLadders(self, board):
        n = len(board)

        def get_pos(num):
            # convert 1-based index to (row, col)
            r = (num - 1) // n
            c = (num - 1) % n

            row = n - 1 - r

            # zigzag logic
            if r % 2 == 0:
                col = c
            else:
                col = n - 1 - c

            return row, col

        visited = set()
        q = deque([(1, 0)])  # (cell, moves)

        while q:
            cell, moves = q.popleft()

            if cell == n * n:
                return moves

            for step in range(1, 7):
                nxt = cell + step

                if nxt > n * n:
                    continue

                r, c = get_pos(nxt)

                if board[r][c] != -1:
                    nxt = board[r][c]

                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, moves + 1))

        return -1