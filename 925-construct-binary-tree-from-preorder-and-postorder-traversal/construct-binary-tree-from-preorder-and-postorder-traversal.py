class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        
        # If only one node
        if len(preorder) == 1:
            return root
        
        # Left subtree root
        left_root_val = preorder[1]
        
        # Find it in postorder
        left_size = postorder.index(left_root_val) + 1
        
        # Build subtrees
        root.left = self.constructFromPrePost(
            preorder[1:1 + left_size],
            postorder[:left_size]
        )
        
        root.right = self.constructFromPrePost(
            preorder[1 + left_size:],
            postorder[left_size:-1]
        )
        
        return root