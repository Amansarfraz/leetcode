# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = None

class Solution(object):
    def pseudoPalindromicPaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, mask):
            if not node:
                return 0

            # Toggle the bit corresponding to the node value
            mask ^= (1 << node.val)

            # If it's a leaf, check if at most one bit is set
            if not node.left and not node.right:
                return 1 if (mask & (mask - 1)) == 0 else 0

            return dfs(node.left, mask) + dfs(node.right, mask)

        return dfs(root, 0)