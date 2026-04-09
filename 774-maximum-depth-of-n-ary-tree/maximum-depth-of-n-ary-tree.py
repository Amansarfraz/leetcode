class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        
        if not root.children:
            return 1
        
        max_depth = 0
        for child in root.children:
            max_depth = max(max_depth, self.maxDepth(child))
        
        return max_depth + 1