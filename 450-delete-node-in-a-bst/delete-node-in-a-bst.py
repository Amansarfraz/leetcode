class Solution(object):
    def deleteNode(self, root, key):
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        else:
            # Node found
            
            # Case 1 & 2: one child or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Case 3: two children
            # Find inorder successor (min in right subtree)
            temp = root.right
            while temp.left:
                temp = temp.left
            
            # Replace value
            root.val = temp.val
            
            # Delete successor
            root.right = self.deleteNode(root.right, temp.val)
        
        return root