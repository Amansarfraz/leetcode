class Solution(object):
    def nthMagicalNumber(self, n, a, b):
        """
        :type n: int
        :type a: int
        :type b: int
        :rtype: int
        """

        MOD = 10**9 + 7

        # manual gcd function
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        lcm = a * b // gcd(a, b)

        def count(x):
            return x // a + x // b - x // lcm

        left, right = 1, min(a, b) * n
        answer = 0

        while left <= right:
            mid = (left + right) // 2

            if count(mid) >= n:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer % MOD