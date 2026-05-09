from collections import Counter

class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        need = [0] * 26

        for word in words2:
            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1

            for i in range(26):
                need[i] = max(need[i], count[i])

        ans = []

        for word in words1:
            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1

            ok = True

            for i in range(26):
                if count[i] < need[i]:
                    ok = False
                    break

            if ok:
                ans.append(word)

        return ans