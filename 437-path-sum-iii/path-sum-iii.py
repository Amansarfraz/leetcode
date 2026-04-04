class Solution(object):
    def pathSum(self, root, targetSum):
        from collections import defaultdict
        
        self.count = 0
        prefix = defaultdict(int)
        prefix[0] = 1  # base case
        
        def dfs(node, curr_sum):
            if not node:
                return
            
            curr_sum += node.val
            
            # check if there is a prefix sum that matches target
            self.count += prefix.get(curr_sum - targetSum, 0)
            
            # add current sum to prefix map
            prefix[curr_sum] += 1
            
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            
            # backtrack
            prefix[curr_sum] -= 1
        
        dfs(root, 0)
        return self.count