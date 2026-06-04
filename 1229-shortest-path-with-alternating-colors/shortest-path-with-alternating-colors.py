from collections import deque

class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        red = [[] for _ in range(n)]
        blue = [[] for _ in range(n)]

        for u, v in redEdges:
            red[u].append(v)

        for u, v in blueEdges:
            blue[u].append(v)

        ans = [-1] * n
        q = deque([(0, 0, -1)])  # node, distance, previous color
        visited = set([(0, -1)])

        while q:
            node, dist, color = q.popleft()

            if ans[node] == -1:
                ans[node] = dist

            if color != 0:  # last edge was not red
                for nei in red[node]:
                    if (nei, 0) not in visited:
                        visited.add((nei, 0))
                        q.append((nei, dist + 1, 0))

            if color != 1:  # last edge was not blue
                for nei in blue[node]:
                    if (nei, 1) not in visited:
                        visited.add((nei, 1))
                        q.append((nei, dist + 1, 1))

        return ans