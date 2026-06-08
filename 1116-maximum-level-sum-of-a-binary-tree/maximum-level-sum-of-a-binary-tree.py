from collections import deque

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        q = deque([root])
        level = 1
        best_level = 1
        max_sum = float('-inf')

        while q:
            level_sum = 0

            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                best_level = level

            level += 1

        return best_level