class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        words = s.split()
        max_len = max(len(word) for word in words)

        res = []

        for i in range(max_len):
            curr = ""
            for word in words:
                if i < len(word):
                    curr += word[i]
                else:
                    curr += " "
            res.append(curr.rstrip())

        return res