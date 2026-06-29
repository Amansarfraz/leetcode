class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        letters = []
        digits = []

        for ch in s:
            if ch.isalpha():
                letters.append(ch)
            else:
                digits.append(ch)

        if abs(len(letters) - len(digits)) > 1:
            return ""

        if len(digits) > len(letters):
            letters, digits = digits, letters

        ans = []

        while letters or digits:
            if letters:
                ans.append(letters.pop())
            if digits:
                ans.append(digits.pop())

        return "".join(ans)