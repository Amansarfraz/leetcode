import heapq

class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events.sort()

        heap = []
        day = 0
        i = 0
        n = len(events)
        attended = 0

        while i < n or heap:
            if not heap:
                day = events[i][0]

            while i < n and events[i][0] <= day:
                heapq.heappush(heap, events[i][1])
                i += 1

            while heap and heap[0] < day:
                heapq.heappop(heap)

            if heap:
                heapq.heappop(heap)
                attended += 1
                day += 1

        return attended