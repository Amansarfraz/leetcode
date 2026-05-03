class Solution(object):
    def subtreeWithAllDeepest(self, root):
        
        def dfs(node):
            if not node:
                return (0, None)  # (depth, subtree_root)
            
            left_depth, left_node = dfs(node.left)
            right_depth, right_node = dfs(node.right)
            
            # If both sides have same depth → current node is answer
            if left_depth == right_depth:
                return (left_depth + 1, node)
            
            # Otherwise return deeper side
            elif left_depth > right_depth:
                return (left_depth + 1, left_node)
            else:
                return (right_depth + 1, right_node)
        
        return dfs(root)[1]