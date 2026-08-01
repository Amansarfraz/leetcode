class Solution(object):
    def minOperationsMaxProfit(self, customers, boardingCost, runningCost):
        """
        :type customers: List[int]
        :type boardingCost: int
        :type runningCost: int
        :rtype: int
        """
        waiting = 0
        profit = 0
        maxProfit = 0
        answer = -1
        rotations = 0
        i = 0

        while i < len(customers) or waiting > 0:
            if i < len(customers):
                waiting += customers[i]
                i += 1

            boarded = min(4, waiting)
            waiting -= boarded

            profit += boarded * boardingCost - runningCost
            rotations += 1

            if profit > maxProfit:
                maxProfit = profit
                answer = rotations

        return answer