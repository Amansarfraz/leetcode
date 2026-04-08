class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7

        # dp[i][a][l] = number of sequences of length i with:
        # a = number of 'A's (0 or 1)
        # l = consecutive 'L's at the end (0,1,2)
        dp = [[[0]*3 for _ in range(2)] for _ in range(n+1)]
        dp[0][0][0] = 1  # Base case: empty string

        for i in range(1, n+1):
            for a in range(2):
                for l in range(3):
                    # Add 'P'
                    dp[i][a][0] = (dp[i][a][0] + dp[i-1][a][l]) % MOD
                    # Add 'A' (only if no 'A' used yet)
                    if a == 1:
                        dp[i][1][0] = (dp[i][1][0] + dp[i-1][0][l]) % MOD
                    # Add 'L' (only if last consecutive L < 2)
                    if l < 2:
                        dp[i][a][l+1] = (dp[i][a][l+1] + dp[i-1][a][l]) % MOD

        # Sum all possibilities of length n
        return sum(dp[n][a][l] for a in range(2) for l in range(3)) % MOD