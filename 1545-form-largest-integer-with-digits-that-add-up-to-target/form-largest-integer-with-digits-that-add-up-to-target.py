class Solution(object):
    def largestNumber(self, cost, target):
        """
        :type cost: List[int]
        :type target: int
        :rtype: str
        """
        dp = [None] * (target + 1)
        dp[0] = ""

        for t in range(1, target + 1):
            for d in range(9, 0, -1):
                c = cost[d - 1]
                if t >= c and dp[t - c] is not None:
                    candidate = dp[t - c] + str(d)
                    if (dp[t] is None or
                        len(candidate) > len(dp[t]) or
                        (len(candidate) == len(dp[t]) and candidate > dp[t])):
                        dp[t] = candidate

        return dp[target] if dp[target] is not None else "0"