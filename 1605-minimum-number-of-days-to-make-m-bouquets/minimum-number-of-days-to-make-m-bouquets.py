class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if m * k > len(bloomDay):
            return -1

        def canMake(days):
            bouquets = 0
            flowers = 0

            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0

            return bouquets >= m

        left, right = min(bloomDay), max(bloomDay)

        while left < right:
            mid = (left + right) // 2

            if canMake(mid):
                right = mid
            else:
                left = mid + 1

        return left