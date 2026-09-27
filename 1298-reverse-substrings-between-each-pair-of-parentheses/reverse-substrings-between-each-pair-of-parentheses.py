class Solution(object):
    def reverseParentheses(self, s):
        """:type s: str :rtype: str"""
        ans = []
        for c in s:
            if c == ')':
                t = []
                while ans[-1] != '(':
                    t.append(ans.pop())
                ans.pop()  # Remove '('
                ans.extend(t)
            else:
                ans.append(c)
        return "".join(ans)
