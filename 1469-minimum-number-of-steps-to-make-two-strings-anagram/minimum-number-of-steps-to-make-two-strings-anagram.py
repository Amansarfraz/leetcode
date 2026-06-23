from collections import Counter

class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        count_s = Counter(s)
        count_t = Counter(t)

        steps = 0

        for ch in count_s:
            if count_s[ch] > count_t[ch]:
                steps += count_s[ch] - count_t[ch]

        return steps