from bisect import bisect_left

class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        jobs = sorted(zip(startTime, endTime, profit))
        starts = [job[0] for job in jobs]
        n = len(jobs)

        dp = [-1] * n

        def dfs(i):
            if i >= n:
                return 0

            if dp[i] != -1:
                return dp[i]

            skip = dfs(i + 1)

            j = bisect_left(starts, jobs[i][1])
            take = jobs[i][2] + dfs(j)

            dp[i] = max(skip, take)
            return dp[i]

        return dfs(0)