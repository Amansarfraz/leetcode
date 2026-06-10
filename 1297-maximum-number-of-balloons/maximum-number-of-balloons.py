class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        from collections import Counter

        cnt = Counter(text)

        return min(
            cnt['b'],
            cnt['a'],
            cnt['l'] // 2,
            cnt['o'] // 2,
            cnt['n']
        )