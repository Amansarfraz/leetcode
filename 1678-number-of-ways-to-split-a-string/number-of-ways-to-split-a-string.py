class Solution(object):
    def numWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        ones = [i for i, ch in enumerate(s) if ch == '1']
        m = len(ones)

        if m == 0:
            n = len(s)
            return ((n - 1) * (n - 2) // 2) % MOD

        if m % 3 != 0:
            return 0

        k = m // 3

        left = ones[k] - ones[k - 1]
        right = ones[2 * k] - ones[2 * k - 1]

        return (left * right) % MOD