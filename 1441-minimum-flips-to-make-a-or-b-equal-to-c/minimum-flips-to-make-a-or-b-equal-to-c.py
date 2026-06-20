class Solution(object):
    def minFlips(self, a, b, c):
        flips = 0

        for i in range(32):  # enough for constraints
            bit_a = (a >> i) & 1
            bit_b = (b >> i) & 1
            bit_c = (c >> i) & 1

            if bit_c == 0:
                # both must be 0
                flips += bit_a + bit_b

            else:
                # at least one must be 1
                if bit_a == 0 and bit_b == 0:
                    flips += 1

        return flips