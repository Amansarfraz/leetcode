class FindElements(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.seen = set()

        def dfs(node, val):
            if not node:
                return

            node.val = val
            self.seen.add(val)

            dfs(node.left, 2 * val + 1)
            dfs(node.right, 2 * val + 2)

        dfs(root, 0)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.seen