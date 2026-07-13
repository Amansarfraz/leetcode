class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        ans = 0
        count = 0

        for ch in s:
            if ch == '1':
                count += 1
                ans += count
            else:
                count = 0

        return ans % MOD