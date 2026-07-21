class Solution(object):
    def longestAwesome(self, s):
        """
        :type s: str
        :rtype: int
        """
        mask = 0
        first = {0: -1}
        ans = 0

        for i, ch in enumerate(s):
            digit = int(ch)
            mask ^= (1 << digit)

            if mask in first:
                ans = max(ans, i - first[mask])
            else:
                first[mask] = i

            for b in range(10):
                new_mask = mask ^ (1 << b)
                if new_mask in first:
                    ans = max(ans, i - first[new_mask])

        return ans