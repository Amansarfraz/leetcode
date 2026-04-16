class Solution(object):
    def trimBST(self, root, low, high):
        if not root:
            return None
        
        # If node is too small → go right
        if root.val < low:
            return self.trimBST(root.right, low, high)
        
        # If node is too large → go left
        if root.val > high:
            return self.trimBST(root.left, low, high)
        
        # Node is valid → trim both sides
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        
        return root