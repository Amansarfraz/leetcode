class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        spaces = text.count(' ')
        words = text.split()

        if len(words) == 1:
            return words[0] + ' ' * spaces

        gap = spaces // (len(words) - 1)
        extra = spaces % (len(words) - 1)

        return (' ' * gap).join(words) + ' ' * extra