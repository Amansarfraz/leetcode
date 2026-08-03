from bisect import bisect_left, insort
import heapq

class Solution(object):
    def busiestServers(self, k, arrival, load):
        """
        :type k: int
        :type arrival: List[int]
        :type load: List[int]
        :rtype: List[int]
        """
        available = list(range(k))
        busy = []
        count = [0] * k

        for i in range(len(arrival)):
            while busy and busy[0][0] <= arrival[i]:
                _, server = heapq.heappop(busy)
                insort(available, server)

            if not available:
                continue

            idx = bisect_left(available, i % k)
            if idx == len(available):
                idx = 0

            server = available.pop(idx)
            count[server] += 1
            heapq.heappush(busy, (arrival[i] + load[i], server))

        mx = max(count)
        return [i for i in range(k) if count[i] == mx]