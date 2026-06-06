# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: Optional[TreeNode]
        :type n: int
        :type x: int
        :rtype: bool
        """
        self.left_size = 0
        self.right_size = 0

        def count(node):
            if not node:
                return 0

            left = count(node.left)
            right = count(node.right)

            if node.val == x:
                self.left_size = left
                self.right_size = right

            return left + right + 1

        count(root)

        parent_side = n - (self.left_size + self.right_size + 1)

        return max(self.left_size, self.right_size, parent_side) > n // 2