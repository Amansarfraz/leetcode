
from collections import deque

class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.root = root
        self.q = deque()

        temp = deque([root])

        while temp:
            node = temp.popleft()

            if not node.left or not node.right:
                self.q.append(node)

            if node.left:
                temp.append(node.left)

            if node.right:
                temp.append(node.right)

    def insert(self, val):
        """
        :type val: int
        :rtype: int
        """
        parent = self.q[0]
        new_node = TreeNode(val)

        if not parent.left:
            parent.left = new_node
        else:
            parent.right = new_node
            self.q.popleft()

        self.q.append(new_node)

        return parent.val

    def get_root(self):
        """
        :rtype: Optional[TreeNode]
        """
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()