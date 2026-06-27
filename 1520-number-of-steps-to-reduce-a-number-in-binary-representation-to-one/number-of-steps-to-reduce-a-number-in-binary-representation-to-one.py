class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        carry = 0
        steps = 0

        for i in range(len(s) - 1, 0, -1):
            bit = int(s[i])

            if bit + carry == 1:
                steps += 2
                carry = 1
            else:
                steps += 1

        return steps + carry