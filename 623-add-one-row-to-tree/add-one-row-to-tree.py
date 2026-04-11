from collections import deque

class Solution(object):
    def addOneRow(self, root, val, depth):
        
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        queue = deque([(root, 1)])

        while queue:
            node, level = queue.popleft()

            if level == depth - 1:
                # insert new nodes
                old_left = node.left
                old_right = node.right

                node.left = TreeNode(val)
                node.right = TreeNode(val)

                node.left.left = old_left
                node.right.right = old_right

            else:
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))

        return root