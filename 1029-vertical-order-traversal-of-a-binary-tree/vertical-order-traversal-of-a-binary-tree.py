# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        
        from collections import defaultdict, deque
        
        nodes = []
        
        def dfs(node, row, col):
            if not node:
                return
            
            nodes.append((col, row, node.val))
            
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
        
        dfs(root, 0, 0)
        
        nodes.sort()
        
        result = defaultdict(list)
        
        for col, row, val in nodes:
            result[col].append(val)
        
        return [result[x] for x in sorted(result)]