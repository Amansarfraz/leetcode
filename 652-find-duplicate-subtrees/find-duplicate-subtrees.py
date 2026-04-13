class Solution(object):
    def findDuplicateSubtrees(self, root):
        
        from collections import defaultdict

        count = defaultdict(int)
        result = []

        def serialize(node):
            if not node:
                return "#"

            serial = (
                str(node.val) + "," +
                serialize(node.left) + "," +
                serialize(node.right)
            )

            count[serial] += 1

            if count[serial] == 2:
                result.append(node)

            return serial

        serialize(root)
        return result