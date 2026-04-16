class Solution(object):
    def findSecondMinimumValue(self, root):
        self.min1 = root.val
        self.ans = float('inf')
        
        def dfs(node):
            if not node:
                return
            
            # only consider values greater than root
            if self.min1 < node.val < self.ans:
                self.ans = node.val
            
            # prune unnecessary branches
            if node.val <= self.ans:
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        
        return self.ans if self.ans != float('inf') else -1