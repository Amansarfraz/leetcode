class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        max_reach = [0] * (n + 1)

        for i in range(n + 1):
            left = max(0, i - ranges[i])
            right = min(n, i + ranges[i])
            max_reach[left] = max(max_reach[left], right)

        taps = 0
        curr_end = 0
        farthest = 0

        for i in range(n + 1):
            if i > farthest:
                return -1

            farthest = max(farthest, max_reach[i])

            if i == curr_end:
                if curr_end == n:
                    break
                taps += 1
                curr_end = farthest

        return taps