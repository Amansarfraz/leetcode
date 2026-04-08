from collections import Counter

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        
        counter = Counter()
        
        def subtree_sum(node):
            if not node:
                return 0
            left = subtree_sum(node.left)
            right = subtree_sum(node.right)
            total = node.val + left + right
            counter[total] += 1
            return total
        
        subtree_sum(root)
        
        if not counter:
            return []
        
        max_freq = max(counter.values())
        return [s for s, freq in counter.items() if freq == max_freq]