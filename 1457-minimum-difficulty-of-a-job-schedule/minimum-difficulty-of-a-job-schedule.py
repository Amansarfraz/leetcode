class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        n = len(jobDifficulty)

        if d > n:
            return -1

        INF = float('inf')

        # dp[i] = min cost for first i jobs (rolling optimization)
        dp = [INF] * (n + 1)
        dp[0] = 0

        for day in range(1, d + 1):
            new_dp = [INF] * (n + 1)

            for i in range(day, n + 1):
                max_d = 0

                for j in range(i, day - 1, -1):
                    max_d = max(max_d, jobDifficulty[j - 1])
                    if dp[j - 1] != INF:
                        new_dp[i] = min(new_dp[i], dp[j - 1] + max_d)

            dp = new_dp

        return dp[n]