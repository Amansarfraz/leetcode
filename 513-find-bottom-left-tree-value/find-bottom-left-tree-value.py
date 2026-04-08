from collections import deque

class Solution(object):
    def findBottomLeftValue(self, root):
        queue = deque([root])
        leftmost = root.val
        
        while queue:
            size = len(queue)
            
            for i in range(size):
                node = queue.popleft()
                
                # first node of this level
                if i == 0:
                    leftmost = node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return leftmost