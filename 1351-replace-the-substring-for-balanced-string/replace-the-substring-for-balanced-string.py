from collections import Counter

class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        target = n // 4
        count = Counter(s)

        if all(count[c] == target for c in "QWER"):
            return 0

        left = 0
        ans = n

        for right in range(n):
            count[s[right]] -= 1

            while left < n and all(count[c] <= target for c in "QWER"):
                ans = min(ans, right - left + 1)
                count[s[left]] += 1
                left += 1

        return ans