class Solution(object):
    def colorBorder(self, grid, row, col, color):
        """
        :type grid: List[List[int]]
        :type row: int
        :type col: int
        :type color: int
        :rtype: List[List[int]]
        """

        rows = len(grid)
        cols = len(grid[0])

        original = grid[row][col]

        visited = set()
        borders = []

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            visited.add((r, c))

            is_border = False

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    is_border = True

                elif grid[nr][nc] != original:
                    is_border = True

                elif (nr, nc) not in visited:
                    dfs(nr, nc)

            if is_border:
                borders.append((r, c))

        dfs(row, col)

        for r, c in borders:
            grid[r][c] = color

        return grid