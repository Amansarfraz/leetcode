class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True:
            product = 1
            x = n

            if x == 0:
                product = 0
            else:
                while x > 0:
                    digit = x % 10
                    product *= digit
                    x //= 10

            if product % t == 0:
                return n

            n += 1