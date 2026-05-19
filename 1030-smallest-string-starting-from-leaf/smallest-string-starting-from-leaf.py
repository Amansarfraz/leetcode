# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: str
        """
        
        self.ans = None
        
        def dfs(node, path):
            if not node:
                return
            
            path = chr(node.val + ord('a')) + path
            
            # Leaf node
            if not node.left and not node.right:
                if self.ans is None or path < self.ans:
                    self.ans = path
            
            dfs(node.left, path)
            dfs(node.right, path)
        
        dfs(root, "")
        
        return self.ans