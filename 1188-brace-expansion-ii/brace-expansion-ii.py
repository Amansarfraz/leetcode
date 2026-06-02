class Solution(object):
    def braceExpansionII(self, expression):
        def product(a, b):
            return {x + y for x in a for y in b}

        stack = []
        curr = {""}
        union = set()

        i = 0
        while i < len(expression):
            ch = expression[i]

            if ch.isalpha():
                j = i
                while j < len(expression) and expression[j].isalpha():
                    j += 1

                word = expression[i:j]
                curr = product(curr, {word})
                i = j - 1

            elif ch == '{':
                stack.append((union, curr))
                union = set()
                curr = {""}

            elif ch == ',':
                union |= curr
                curr = {""}

            elif ch == '}':
                union |= curr
                prev_union, prev_curr = stack.pop()

                curr = product(prev_curr, union)
                union = prev_union

            i += 1

        result = sorted(list(union | curr))
        return result