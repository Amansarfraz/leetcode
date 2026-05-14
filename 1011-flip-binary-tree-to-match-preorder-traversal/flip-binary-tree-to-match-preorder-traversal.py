# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: Optional[TreeNode]
        :type voyage: List[int]
        :rtype: List[int]
        """
        
        self.i = 0
        res = []
        
        def dfs(node):
            if not node:
                return True
            
            if node.val != voyage[self.i]:
                return False
            
            self.i += 1
            
            if node.left and self.i < len(voyage) and node.left.val != voyage[self.i]:
                res.append(node.val)
                node.left, node.right = node.right, node.left
            
            return dfs(node.left) and dfs(node.right)
        
        return res if dfs(root) else [-1]