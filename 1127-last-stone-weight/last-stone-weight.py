import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        # Max heap banane ke liye negative values use karenge
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            # Agar dono stones equal nahi hain
            if first != second:
                heapq.heappush(stones, -(first - second))

        return -stones[0] if stones else 0