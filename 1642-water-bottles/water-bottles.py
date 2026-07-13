class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        ans = 0
        empty = 0

        while numBottles > 0:
            ans += numBottles
            empty += numBottles

            numBottles = empty // numExchange
            empty %= numExchange

        return ans
        