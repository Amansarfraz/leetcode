class Solution(object):
    def distinctSubseqII(self, s):
        """:type s: str :rtype: int"""
        MOD = 10**9 + 7
        result, dp = 0, [0] * 26
        for c in s:
            idx = ord(c) - ord('a')
            result, dp[idx] = (result + ((result + 1) - dp[idx])) % MOD, (result + 1) % MOD
        return result
