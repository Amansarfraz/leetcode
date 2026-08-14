from collections import Counter

class Solution(object):
    def maximumLengthSubstring(self, s):
        """:type s: str :rtype: int"""
        count = Counter()
        ans = left = 0
        for right, c in enumerate(s):
            count[c] += 1
            while count[c] > 2:
                count[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans