class Solution(object):
    def increasingBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self.curr = TreeNode(0)   # dummy node
        self.head = self.curr     # to return result

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            node.left = None              # remove left
            self.curr.right = node        # attach node
            self.curr = node              # move pointer
            
            inorder(node.right)
        
        inorder(root)
        return self.head.right