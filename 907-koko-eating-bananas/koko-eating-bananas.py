import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        def can_eat(k):
            hours = 0
            for p in piles:
                hours += (p + k - 1) // k  # ceil(p/k)
            return hours <= h

        left, right = 1, max(piles)
        answer = right

        while left <= right:
            mid = (left + right) // 2

            if can_eat(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer