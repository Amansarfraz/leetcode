import heapq

class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        heap = []

        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))

        ans = []

        while heap:
            cnt1, ch1 = heapq.heappop(heap)

            if len(ans) >= 2 and ans[-1] == ch1 and ans[-2] == ch1:
                if not heap:
                    break

                cnt2, ch2 = heapq.heappop(heap)
                ans.append(ch2)
                cnt2 += 1

                if cnt2 < 0:
                    heapq.heappush(heap, (cnt2, ch2))
                heapq.heappush(heap, (cnt1, ch1))
            else:
                ans.append(ch1)
                cnt1 += 1

                if cnt1 < 0:
                    heapq.heappush(heap, (cnt1, ch1))

        return "".join(ans)