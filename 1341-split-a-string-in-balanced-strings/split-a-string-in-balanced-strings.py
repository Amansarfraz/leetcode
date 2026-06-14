class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        balance = 0
        count = 0

        for ch in s:
            if ch == 'R':
                balance += 1
            else:  # 'L'
                balance -= 1

            if balance == 0:
                count += 1

        return count