class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        score = 0
        first_seen = {}
        ans = 0

        for i, h in enumerate(hours):
            if h > 8:
                score += 1
            else:
                score -= 1

            if score > 0:
                ans = i + 1
            else:
                if score - 1 in first_seen:
                    ans = max(ans, i - first_seen[score - 1])

            if score not in first_seen:
                first_seen[score] = i

        return ans