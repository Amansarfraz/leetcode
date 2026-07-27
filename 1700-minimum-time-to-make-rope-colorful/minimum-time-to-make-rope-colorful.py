class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        ans = 0
        maxTime = neededTime[0]

        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                ans += min(maxTime, neededTime[i])
                maxTime = max(maxTime, neededTime[i])
            else:
                maxTime = neededTime[i]

        return ans