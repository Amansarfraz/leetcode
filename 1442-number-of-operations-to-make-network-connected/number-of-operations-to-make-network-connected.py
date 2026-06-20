class Solution(object):
    def makeConnected(self, n, connections):
        if len(connections) < n - 1:
            return -1

        from collections import defaultdict

        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            stack = [node]
            while stack:
                cur = stack.pop()
                for nei in graph[cur]:
                    if nei not in visited:
                        visited.add(nei)
                        stack.append(nei)

        components = 0

        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                components += 1

        return components - 1