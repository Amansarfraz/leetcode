class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        curr = ""

        for ch in s:
            if ch == '(':
                stack.append(curr)
                curr = ""
            elif ch == ')':
                curr = stack.pop() + curr[::-1]
            else:
                curr += ch

        return curr