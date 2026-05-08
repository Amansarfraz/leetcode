class Solution(object):
    def atMostNGivenDigitSet(self, digits, n):
        s = str(n)
        m = len(s)
        d = len(digits)

        result = 0

        # Count numbers with smaller lengths
        for length in range(1, m):
            result += d ** length

        # Count numbers with same length
        for i in range(m):
            smaller = 0

            for digit in digits:
                if digit < s[i]:
                    smaller += 1

            result += smaller * (d ** (m - i - 1))

            # If current digit not available, stop
            if s[i] not in digits:
                return result

        # n itself is valid
        return result + 1