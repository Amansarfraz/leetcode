class Solution(object):
    def distinctEchoSubstrings(self, text):
        """
        :type text: str
        :rtype: int
        """
        n = len(text)
        seen = set()

        for length in range(1, n // 2 + 1):
            for i in range(n - 2 * length + 1):
                if text[i:i + length] == text[i + length:i + 2 * length]:
                    seen.add(text[i:i + length])

        return len(seen)