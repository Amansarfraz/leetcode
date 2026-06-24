class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        parent = [-1] * n

        for i in range(n):
            for child in (leftChild[i], rightChild[i]):
                if child != -1:
                    if parent[child] != -1:
                        return False
                    parent[child] = i

        roots = [i for i in range(n) if parent[i] == -1]
        if len(roots) != 1:
            return False

        root = roots[0]
        visited = set()
        stack = [root]

        while stack:
            node = stack.pop()

            if node in visited:
                return False

            visited.add(node)

            if leftChild[node] != -1:
                stack.append(leftChild[node])

            if rightChild[node] != -1:
                stack.append(rightChild[node])

        return len(visited) == n