class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = [0, 0, 0]
        left = 0
        res = 0

        for right in range(len(s)):
            count[ord(s[right]) - ord('a')] += 1

            while count[0] > 0 and count[1] > 0 and count[2] > 0:
                res += len(s) - right
                count[ord(s[left]) - ord('a')] -= 1
                left += 1

        return res