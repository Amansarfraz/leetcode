class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        def match(listNode, treeNode):
            if not listNode:
                return True
            if not treeNode:
                return False
            if listNode.val != treeNode.val:
                return False

            return (match(listNode.next, treeNode.left) or
                    match(listNode.next, treeNode.right))

        def dfs(node):
            if not node:
                return False

            return (match(head, node) or
                    dfs(node.left) or
                    dfs(node.right))

        return dfs(root)