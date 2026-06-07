from collections import Counter

class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        count = Counter(text)

        groups = []
        i = 0
        n = len(text)

        while i < n:
            j = i
            while j < n and text[j] == text[i]:
                j += 1
            groups.append((text[i], j - i))
            i = j

        ans = 0

        for ch, length in groups:
            ans = max(ans, min(length + (count[ch] > length), count[ch]))

        for i in range(1, len(groups) - 1):
            if groups[i][1] == 1 and groups[i - 1][0] == groups[i + 1][0]:
                ch = groups[i - 1][0]
                merged = groups[i - 1][1] + groups[i + 1][1]

                if count[ch] > merged:
                    merged += 1

                ans = max(ans, merged)

        return ans