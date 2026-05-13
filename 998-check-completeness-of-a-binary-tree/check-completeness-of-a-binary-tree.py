# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        q = deque([root])
        found_null = False

        while q:
            node = q.popleft()

            if node is None:
                found_null = True
            else:
                if found_null:
                    return False

                q.append(node.left)
                q.append(node.right)

        return True