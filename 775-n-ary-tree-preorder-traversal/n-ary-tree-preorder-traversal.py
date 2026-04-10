class Solution(object):
    def preorder(self, root):
        res = []
        
        def dfs(node):
            if not node:
                return
            
            res.append(node.val)   # Visit root
            
            for child in node.children:  # Visit children
                dfs(child)
        
        dfs(root)
        return res