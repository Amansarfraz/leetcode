import heapq

class Solution(object):
    def reachableNodes(self, edges, maxMoves, n):
        """
        :type edges: List[List[int]]
        :type maxMoves: int
        :type n: int
        :rtype: int
        """

        graph = {i: [] for i in range(n)}

        # build graph with weights
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # Dijkstra-like max heap (store remaining moves)
        heap = [(-maxMoves, 0)]  # (remaining_moves, node)
        best = {}

        used = {}

        visited_nodes = 0

        while heap:
            moves, node = heapq.heappop(heap)
            moves = -moves

            if node in best and best[node] >= moves:
                continue

            best[node] = moves
            visited_nodes += 1

            for nei, w in graph[node]:

                used_key = (node, nei)
                used_steps = min(moves, w)

                used[used_key] = max(used.get(used_key, 0), used_steps)

                if moves > w:
                    heapq.heappush(heap, (-(moves - w - 1), nei))

        # count reachable subdivided nodes
        result = visited_nodes

        for u, v, w in edges:
            result += min(w, used.get((u, v), 0) + used.get((v, u), 0))

        return result