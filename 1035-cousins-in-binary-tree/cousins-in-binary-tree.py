# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """
        from collections import deque

        queue = deque([(root, None)])

        while queue:
            size = len(queue)
            parent_x = None
            parent_y = None

            for _ in range(size):
                node, parent = queue.popleft()

                if node.val == x:
                    parent_x = parent

                if node.val == y:
                    parent_y = parent

                if node.left:
                    queue.append((node.left, node))

                if node.right:
                    queue.append((node.right, node))

            if parent_x and parent_y:
                return parent_x != parent_y

            if parent_x or parent_y:
                return False

        return False