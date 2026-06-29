class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        rightOnes = s.count('1')
        leftZeros = 0
        ans = 0

        for i in range(len(s) - 1):
            if s[i] == '0':
                leftZeros += 1
            else:
                rightOnes -= 1

            ans = max(ans, leftZeros + rightOnes)

        return ans