# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.diameter = 0  # Global variable to track max diameter

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            # Update diameter at this node
            self.diameter = max(self.diameter, left + right)
            # Return max depth for parent use
            return 1 + max(left, right)

        dfs(root)
        return self.diameter