class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Condition 1: At most one 'A'
        if s.count('A') > 1:
            return False
        # Condition 2: No three consecutive 'L's
        if 'LLL' in s:
            return False
        return True