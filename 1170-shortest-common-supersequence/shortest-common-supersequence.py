class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        m, n = len(str1), len(str2)

        # Longest Common Subsequence DP
        dp = [[""] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                if str1[i] == str2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + str1[i]
                else:
                    if len(dp[i][j + 1]) > len(dp[i + 1][j]):
                        dp[i + 1][j + 1] = dp[i][j + 1]
                    else:
                        dp[i + 1][j + 1] = dp[i + 1][j]

        lcs = dp[m][n]

        # Build shortest common supersequence using LCS
        ans = []
        i = j = 0

        for ch in lcs:
            while str1[i] != ch:
                ans.append(str1[i])
                i += 1

            while str2[j] != ch:
                ans.append(str2[j])
                j += 1

            ans.append(ch)
            i += 1
            j += 1

        ans.append(str1[i:])
        ans.append(str2[j:])

        return "".join(ans)