class Solution(object):
    def postorder(self, root):
        res = []
        
        def dfs(node):
            if not node:
                return
            
            # First visit all children
            for child in node.children:
                dfs(child)
            
            # Then visit root
            res.append(node.val)
        
        dfs(root)
        return res