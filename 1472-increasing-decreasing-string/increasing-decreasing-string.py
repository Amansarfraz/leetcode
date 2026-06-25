from collections import Counter

class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s)
        ans = []

        while len(ans) < len(s):
            # increasing order
            for ch in sorted(count):
                if count[ch] > 0:
                    ans.append(ch)
                    count[ch] -= 1

            # decreasing order
            for ch in sorted(count, reverse=True):
                if count[ch] > 0:
                    ans.append(ch)
                    count[ch] -= 1

        return "".join(ans)