class Solution(object):
    def numTimesAllBlue(self, flips):
        """
        :type flips: List[int]
        :rtype: int
        """
        ans = 0
        mx = 0

        for i, bulb in enumerate(flips):
            mx = max(mx, bulb)

            if mx == i + 1:
                ans += 1

        return ans