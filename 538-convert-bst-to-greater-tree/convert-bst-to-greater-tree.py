# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def convertBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self.total = 0
        
        def reverse_inorder(node):
            if not node:
                return
            # Visit right subtree first
            reverse_inorder(node.right)
            # Update current node
            self.total += node.val
            node.val = self.total
            # Visit left subtree
            reverse_inorder(node.left)
        
        reverse_inorder(root)
        return root