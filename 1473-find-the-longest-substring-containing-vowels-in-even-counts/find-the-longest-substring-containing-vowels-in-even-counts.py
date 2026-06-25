class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        pos = {0: -1}  # mask -> first index
        mask = 0
        ans = 0

        vowels = {
            'a': 0,
            'e': 1,
            'i': 2,
            'o': 3,
            'u': 4
        }

        for i, ch in enumerate(s):
            if ch in vowels:
                mask ^= (1 << vowels[ch])

            if mask in pos:
                ans = max(ans, i - pos[mask])
            else:
                pos[mask] = i

        return ans