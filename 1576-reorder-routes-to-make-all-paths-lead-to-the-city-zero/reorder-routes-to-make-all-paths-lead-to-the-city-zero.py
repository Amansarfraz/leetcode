class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        graph = [[] for _ in range(n)]
        directed = set()

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
            directed.add((u, v))

        visited = [False] * n
        stack = [0]
        visited[0] = True
        ans = 0

        while stack:
            node = stack.pop()
            for nei in graph[node]:
                if not visited[nei]:
                    if (node, nei) in directed:
                        ans += 1
                    visited[nei] = True
                    stack.append(nei)

        return ans