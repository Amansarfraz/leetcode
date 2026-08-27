from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
            
        queue = deque([root])
        level = 0
        
        while queue:
            level_size = len(queue)
            # Initialize a variable to track the previous node's value in this level
            prev_val = None
            
            for _ in range(level_size):
                node = queue.popleft()
                val = node.val
                
                # Rule 1: Check if parity matches the level index
                if level % 2 == 0:
                    # Even level -> values must be ODD
                    if val % 2 == 0:
                        return False
                    # Even level -> values must be STRICTLY INCREASING
                    if prev_val is not None and val <= prev_val:
                        return False
                else:
                    # Odd level -> values must be EVEN
                    if val % 2 != 0:
                        return False
                    # Odd level -> values must be STRICTLY DECREASING
                    if prev_val is not None and val >= prev_val:
                        return False
                
                # Update the previous value for the next iteration in this level
                prev_val = val
                
                # Append child nodes to queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            # Move to the next level index
            level += 1
            
        return True
