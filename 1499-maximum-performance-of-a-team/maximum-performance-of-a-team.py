import heapq

class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7

        engineers = sorted(zip(efficiency, speed), reverse=True)

        heap = []
        speed_sum = 0
        ans = 0

        for eff, spd in engineers:
            if len(heap) == k:
                speed_sum -= heapq.heappop(heap)

            heapq.heappush(heap, spd)
            speed_sum += spd

            ans = max(ans, speed_sum * eff)

        return ans % MOD