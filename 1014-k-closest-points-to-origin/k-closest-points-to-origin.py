import heapq

class Solution(object):
    def kClosest(self, points, k):
        heap = []

        for x, y in points:
            heapq.heappush(heap, (x*x + y*y, [x, y]))

        return [heapq.heappop(heap)[1] for _ in range(k)]