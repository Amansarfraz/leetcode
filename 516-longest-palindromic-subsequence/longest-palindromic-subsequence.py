class Solution(object):
    def longestPalindromeSubseq(self, s):
        n = len(s)
        
        # dp[i][j] = LPS length in s[i...j]
        dp = [[0] * n for _ in range(n)]
        
        # single characters are palindrome of length 1
        for i in range(n):
            dp[i][i] = 1
        
        # fill table
        for length in range(2, n + 1):  # substring length
            for i in range(n - length + 1):
                j = i + length - 1
                
                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        return dp[0][n-1]