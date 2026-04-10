class Solution(object):
    def fractionAddition(self, expression):
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return abs(a)

        num = 0
        den = 1
        i = 0
        n = len(expression)

        while i < n:
            sign = 1
            if expression[i] in "+-":
                if expression[i] == "-":
                    sign = -1
                i += 1

            num2 = 0
            while i < n and expression[i].isdigit():
                num2 = num2 * 10 + int(expression[i])
                i += 1

            i += 1  # skip '/'

            den2 = 0
            while i < n and expression[i].isdigit():
                den2 = den2 * 10 + int(expression[i])
                i += 1

            num2 *= sign

            # add fractions
            num = num * den2 + num2 * den
            den = den * den2

            # reduce
            g = gcd(num, den)
            num //= g
            den //= g

        # fix sign
        if den < 0:
            num = -num
            den = -den

        return str(num) + "/" + str(den)