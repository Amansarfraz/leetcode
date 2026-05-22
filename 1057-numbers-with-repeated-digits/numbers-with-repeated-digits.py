class Solution(object):
    def numDupDigitsAtMostN(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        digits = list(map(int, str(n + 1)))
        length = len(digits)

        def perm(m, k):
            ans = 1
            for i in range(k):
                ans *= (m - i)
            return ans

        unique = 0

        # Count unique-digit numbers with smaller length
        for i in range(1, length):
            unique += 9 * perm(9, i - 1)

        # Count unique-digit numbers with same length
        used = set()

        for i in range(length):
            for d in range(0 if i else 1, digits[i]):
                if d in used:
                    continue

                unique += perm(9 - i, length - i - 1)

            if digits[i] in used:
                break

            used.add(digits[i])

        return n - unique