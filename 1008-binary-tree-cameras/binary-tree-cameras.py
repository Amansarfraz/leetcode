# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        self.cameras = 0
        
        # 0 = needs camera
        # 1 = has camera
        # 2 = covered
        
        def dfs(node):
            if not node:
                return 2
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left == 0 or right == 0:
                self.cameras += 1
                return 1
            
            if left == 1 or right == 1:
                return 2
            
            return 0
        
        if dfs(root) == 0:
            self.cameras += 1
        
        return self.cameras