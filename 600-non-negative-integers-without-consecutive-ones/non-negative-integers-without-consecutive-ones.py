class Solution(object):
    def findIntegers(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Step 1: build Fibonacci DP for valid binary strings
        # dp[i] = number of valid binary strings of length i
        dp = [0] * 32
        dp[0], dp[1] = 1, 2  # 0, 1

        for i in range(2, 32):
            dp[i] = dp[i - 1] + dp[i - 2]

        # Step 2: traverse bits of n
        prev_bit = 0
        result = 0

        for i in range(30, -1, -1):
            if n & (1 << i):
                result += dp[i]
                if prev_bit == 1:
                    return result
                prev_bit = 1
            else:
                prev_bit = 0

        return result + 1