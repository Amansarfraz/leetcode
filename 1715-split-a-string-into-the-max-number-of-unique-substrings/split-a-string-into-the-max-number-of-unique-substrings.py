class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        used = set()
        n = len(s)

        def backtrack(start):
            if start == n:
                return 0

            ans = 0

            for end in range(start + 1, n + 1):
                sub = s[start:end]

                if sub not in used:
                    used.add(sub)
                    ans = max(ans, 1 + backtrack(end))
                    used.remove(sub)

            return ans

        return backtrack(0)