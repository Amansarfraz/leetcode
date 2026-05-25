# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def recoverFromPreorder(self, traversal):
        """
        :type traversal: str
        :rtype: Optional[TreeNode]
        """

        stack = []
        i = 0
        n = len(traversal)

        while i < n:

            depth = 0
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1

            value = 0
            while i < n and traversal[i].isdigit():
                value = value * 10 + int(traversal[i])
                i += 1

            node = TreeNode(value)

            while len(stack) > depth:
                stack.pop()

            if stack:
                parent = stack[-1]

                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node

            stack.append(node)

        return stack[0]