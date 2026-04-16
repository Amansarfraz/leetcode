class Solution(object):
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        
        from collections import deque
        queue = deque([(root, 0)])  # (node, index)
        max_width = 0
        
        while queue:
            level_length = len(queue)
            _, first_index = queue[0]
            
            for i in range(level_length):
                node, index = queue.popleft()
                
                # normalize index to prevent overflow
                index -= first_index
                
                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))
                
                # last node gives width
                if i == level_length - 1:
                    max_width = max(max_width, index + 1)
        
        return max_width