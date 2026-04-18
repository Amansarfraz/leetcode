import heapq

class Solution(object):
    def networkDelayTime(self, times, n, k):
        # build graph
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))

        # min heap (time, node)
        heap = [(0, k)]
        dist = {}

        while heap:
            time, node = heapq.heappop(heap)

            if node in dist:
                continue

            dist[node] = time

            for nei, w in graph[node]:
                if nei not in dist:
                    heapq.heappush(heap, (time + w, nei))

        # check all nodes reached
        if len(dist) != n:
            return -1

        return max(dist.values())