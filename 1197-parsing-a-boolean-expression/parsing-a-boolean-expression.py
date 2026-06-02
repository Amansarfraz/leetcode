class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        stack = []

        for ch in expression:
            if ch == ',':
                continue

            if ch != ')':
                stack.append(ch)
            else:
                vals = set()

                while stack[-1] != '(':
                    vals.add(stack.pop())

                stack.pop()  # remove '('
                op = stack.pop()

                if op == '!':
                    stack.append('t' if 'f' in vals else 'f')
                elif op == '&':
                    stack.append('t' if vals == {'t'} else 'f')
                else:  # op == '|'
                    stack.append('t' if 't' in vals else 'f')

        return stack[-1] == 't'
        