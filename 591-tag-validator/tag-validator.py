class Solution(object):
    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
        stack = []
        i = 0
        n = len(code)

        def is_valid_tag_name(tag):
            if not (1 <= len(tag) <= 9):
                return False
            return tag.isalpha() and tag.isupper()

        while i < n:
            if i > 0 and not stack:
                return False  # content outside root tag

            if code.startswith("<![CDATA[", i):
                j = i + 9
                k = code.find("]]>", j)
                if k == -1:
                    return False
                i = k + 3

            elif code.startswith("</", i):
                j = code.find(">", i)
                if j == -1:
                    return False
                tag = code[i+2:j]
                if not stack or stack[-1] != tag:
                    return False
                stack.pop()
                i = j + 1

            elif code.startswith("<", i):
                j = code.find(">", i)
                if j == -1:
                    return False
                tag = code[i+1:j]
                if not is_valid_tag_name(tag):
                    return False
                stack.append(tag)
                i = j + 1

            else:
                i += 1

        return not stack