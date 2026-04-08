class Solution(object):
    def findMode(self, root):
        if not root:
            return []

        # Use list/dict to hold mutable values
        state = {
            "current_val": None,
            "current_count": 0,
            "max_count": 0,
            "modes": []
        }

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            # update count
            if node.val == state["current_val"]:
                state["current_count"] += 1
            else:
                state["current_val"] = node.val
                state["current_count"] = 1
            
            # update modes
            if state["current_count"] > state["max_count"]:
                state["max_count"] = state["current_count"]
                state["modes"] = [state["current_val"]]
            elif state["current_count"] == state["max_count"]:
                state["modes"].append(state["current_val"])
            
            inorder(node.right)
        
        inorder(root)
        return state["modes"]