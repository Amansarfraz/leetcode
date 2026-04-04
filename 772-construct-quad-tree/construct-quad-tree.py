class Solution(object):
    def construct(self, grid):
        
        def build(r, c, size):
            # Check if all values are same
            first = grid[r][c]
            is_leaf = True
            
            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != first:
                        is_leaf = False
                        break
                if not is_leaf:
                    break
            
            # If uniform → leaf node
            if is_leaf:
                return Node(first == 1, True)
            
            # Otherwise split into 4 parts
            half = size // 2
            
            topLeft = build(r, c, half)
            topRight = build(r, c + half, half)
            bottomLeft = build(r + half, c, half)
            bottomRight = build(r + half, c + half, half)
            
            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)
        
        return build(0, 0, len(grid))