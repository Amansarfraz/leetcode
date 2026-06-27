class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        satisfaction.sort()

        suffixSum = 0
        ans = 0

        for i in range(len(satisfaction) - 1, -1, -1):
            suffixSum += satisfaction[i]
            if suffixSum <= 0:
                break
            ans += suffixSum

        return ans