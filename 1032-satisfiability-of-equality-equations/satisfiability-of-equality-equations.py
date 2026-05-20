class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        parent = list(range(26))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        # First process all "==" equations
        for eq in equations:
            if eq[1:3] == "==":
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')
                union(x, y)

        # Then check all "!=" equations
        for eq in equations:
            if eq[1:3] == "!=":
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')

                if find(x) == find(y):
                    return False

        return True