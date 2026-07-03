class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        words = text.lower().split()
        words.sort(key=len)
        words[0] = words[0].capitalize()
        return " ".join(words)