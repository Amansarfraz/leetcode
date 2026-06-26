import math

class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def divisor_sum(num):
            divisors = set()

            for i in range(1, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    divisors.add(i)
                    divisors.add(num // i)

                    if len(divisors) > 4:
                        return 0

            if len(divisors) == 4:
                return sum(divisors)
            return 0

        ans = 0
        for num in nums:
            ans += divisor_sum(num)

        return ans