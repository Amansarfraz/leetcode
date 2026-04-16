class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        parent = {}
        candidate1 = None
        candidate2 = None

        # step 1: detect node with 2 parents
        par = {}

        for u, v in edges:
            if v in par:
                candidate1 = [par[v], v]
                candidate2 = [u, v]
            else:
                par[v] = u

        # DSU
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return False
            parent[rootB] = rootA
            return True

        # initialize DSU
        for u, v in edges:
            parent[u] = u
            parent[v] = v

        # step 2: union edges (skip candidate2 if exists)
        for u, v in edges:
            if [u, v] == candidate2:
                continue

            if not union(u, v):
                # cycle found
                if candidate1:
                    return candidate1
                return [u, v]

        # step 3: if no cycle found, remove candidate2
        return candidate2