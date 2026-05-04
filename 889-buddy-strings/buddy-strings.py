class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """

        # Step 1: length check
        if len(s) != len(goal):
            return False

        # Step 2: if strings are equal
        if s == goal:
            # check duplicate character exists
            return len(set(s)) < len(s)

        # Step 3: find mismatched positions
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)

        # must have exactly 2 differences
        if len(diff) != 2:
            return False

        i, j = diff

        # swapping should fix it
        return s[i] == goal[j] and s[j] == goal[i]