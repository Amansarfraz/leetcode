class Solution(object):
    def countSubgraphsForEachDiameter(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        graph = [[] for _ in range(n)]

        for u, v in edges:
            u -= 1
            v -= 1
            graph[u].append(v)
            graph[v].append(u)

        answer = [0] * (n - 1)

        # Check every subset of cities
        for mask in range(1, 1 << n):

            # A valid subtree must have at least 2 cities
            if mask & (mask - 1) == 0:
                continue

            # Find one city in the subset
            start = -1
            for i in range(n):
                if mask & (1 << i):
                    start = i
                    break

            # Check connectivity and find farthest node from start
            def bfs(source):
                dist = [-1] * n
                dist[source] = 0
                queue = [source]
                farthest = source

                for node in queue:
                    for nei in graph[node]:
                        if (mask & (1 << nei)) and dist[nei] == -1:
                            dist[nei] = dist[node] + 1
                            queue.append(nei)

                            if dist[nei] > dist[farthest]:
                                farthest = nei

                return farthest, dist[farthest], len(queue)

            farthest, _, count = bfs(start)

            # If not all selected nodes are connected, skip
            selected_count = 0
            for i in range(n):
                if mask & (1 << i):
                    selected_count += 1

            if count != selected_count:
                continue

            # Diameter = maximum distance from farthest node
            _, diameter, _ = bfs(farthest)

            answer[diameter - 1] += 1

        return answer

