# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(a, b):
            if not a and not b:
                return True
            if not a or not b or a.val != b.val:
                return False
            
            # no flip OR flip case
            return (
                (dfs(a.left, b.left) and dfs(a.right, b.right)) or
                (dfs(a.left, b.right) and dfs(a.right, b.left))
            )
        
        return dfs(root1, root2)