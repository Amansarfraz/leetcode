class Solution(object):
    def allPossibleFBT(self, n):
        memo = {}
        
        def solve(n):
            if n in memo:
                return memo[n]
            
            if n == 1:
                return [TreeNode(0)]
            
            if n % 2 == 0:
                return []
            
            res = []
            
            for left_nodes in range(1, n, 2):
                right_nodes = n - 1 - left_nodes
                
                left_trees = solve(left_nodes)
                right_trees = solve(right_nodes)
                
                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(0)
                        root.left = l
                        root.right = r
                        res.append(root)
            
            memo[n] = res
            return res
        
        return solve(n)