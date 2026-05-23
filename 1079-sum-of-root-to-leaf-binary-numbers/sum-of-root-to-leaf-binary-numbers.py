# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        # DFS traversal
        def dfs(node, current):
            
            if not node:
                return 0
            
            # Build binary number
            current = current * 2 + node.val
            
            # Leaf node
            if not node.left and not node.right:
                return current
            
            # Sum from left and right subtree
            return dfs(node.left, current) + dfs(node.right, current)
        
        
        return dfs(root, 0)