# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """

        def get_leaves(root, leaves):
            if not root:
                return

            # if leaf node
            if not root.left and not root.right:
                leaves.append(root.val)
                return

            get_leaves(root.left, leaves)
            get_leaves(root.right, leaves)

        leaves1 = []
        leaves2 = []

        get_leaves(root1, leaves1)
        get_leaves(root2, leaves2)

        return leaves1 == leaves2