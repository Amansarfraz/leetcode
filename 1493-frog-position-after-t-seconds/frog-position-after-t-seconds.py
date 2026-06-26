from collections import defaultdict

class Solution(object):
    def frogPosition(self, n, edges, t, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type t: int
        :type target: int
        :rtype: float
        """
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, parent, time, prob):
            if time == t:
                if node == target:
                    return prob
                return 0.0

            children = 0
            for nei in graph[node]:
                if nei != parent:
                    children += 1

            # No unvisited children
            if children == 0:
                if node == target:
                    return prob
                return 0.0

            for nei in graph[node]:
                if nei != parent:
                    ans = dfs(nei, node, time + 1, prob / children)
                    if ans > 0:
                        return ans

            return 0.0

        return dfs(1, 0, 0, 1.0)