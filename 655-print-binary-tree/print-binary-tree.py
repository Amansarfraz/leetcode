import math

class Solution(object):
    def printTree(self, root):
        
        # height of tree
        def get_height(node):
            if not node:
                return -1
            return 1 + max(get_height(node.left), get_height(node.right))

        height = get_height(root)
        rows = height + 1
        cols = (2 ** (height + 1)) - 1

        # create grid
        res = [["" for _ in range(cols)] for _ in range(rows)]

        # fill function
        def fill(node, r, c, offset):
            if not node:
                return

            res[r][c] = str(node.val)

            if node.left:
                fill(node.left, r + 1, c - offset, offset // 2)
            if node.right:
                fill(node.right, r + 1, c + offset, offset // 2)

        fill(root, 0, (cols - 1) // 2, (cols + 1) // 4)

        return res