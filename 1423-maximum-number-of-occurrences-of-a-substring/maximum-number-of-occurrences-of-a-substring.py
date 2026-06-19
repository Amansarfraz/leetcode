from collections import Counter, defaultdict

class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        freq = defaultdict(int)
        count = Counter()
        left = 0

        for right in range(len(s)):
            count[s[right]] += 1

            if right - left + 1 > minSize:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1

            if right - left + 1 == minSize:
                if len(count) <= maxLetters:
                    freq[s[left:right + 1]] += 1

        return max(freq.values()) if freq else 0