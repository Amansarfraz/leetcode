class Solution(object):
    def pruneTree(self, root):
        if not root:
            return None
        
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        
        # If current node is 0 and both children are None → delete it
        if root.val == 0 and not root.left and not root.right:
            return None
        
        return root