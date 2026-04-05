from collections import deque

class Codec:

    def serialize(self, root):
        if not root:
            return ""
        
        res = []
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        
        return ",".join(res)

    def deserialize(self, data):
        if not data:
            return None
        
        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        queue = deque([root])
        i = 1
        
        while queue:
            node = queue.popleft()
            
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        
        return root