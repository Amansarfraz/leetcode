class Solution(object):
    def dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7

        # dp[face][count] for current step
        dp = [[0] * (max(rollMax) + 1) for _ in range(6)]

        # initialize first roll
        for f in range(6):
            dp[f][1] = 1

        for _ in range(2, n + 1):
            new_dp = [[0] * (max(rollMax) + 1) for _ in range(6)]

            for f in range(6):
                for prev_f in range(6):
                    for cnt in range(1, rollMax[prev_f] + 1):
                        val = dp[prev_f][cnt]
                        if val == 0:
                            continue

                        if f == prev_f:
                            if cnt + 1 <= rollMax[f]:
                                new_dp[f][cnt + 1] = (new_dp[f][cnt + 1] + val) % MOD
                        else:
                            new_dp[f][1] = (new_dp[f][1] + val) % MOD

            dp = new_dp

        result = 0
        for f in range(6):
            for cnt in range(1, rollMax[f] + 1):
                result = (result + dp[f][cnt]) % MOD

        return result