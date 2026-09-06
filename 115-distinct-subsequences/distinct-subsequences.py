class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        # dp[i][j] represents the number of distinct subsequences of s[:i] which equals t[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # An empty string t can always be formed once by any prefix of s
        for i in range(m + 1):
            dp[i][0] = 1
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    # Match current characters or skip the character in s
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    # Characters do not match, skip the character in s
                    dp[i][j] = dp[i - 1][j]
                    
        return dp[m][n]
