class Solution(object):
    def longestDecomposition(self, text):
        """
        :type text: str
        :rtype: int
        """
        left = ""
        right = ""
        ans = 0

        n = len(text)

        for i in range(n):
            left += text[i]
            right = text[n - 1 - i] + right

            if left == right:
                ans += 1
                left = ""
                right = ""

        return ans