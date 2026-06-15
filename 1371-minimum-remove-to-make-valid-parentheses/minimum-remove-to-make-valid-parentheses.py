class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        stack = []

        # Step 1: remove invalid ')'
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''  # remove invalid ')'

        # Step 2: remove unmatched '('
        while stack:
            s[stack.pop()] = ''

        return ''.join(s)