class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        def pos(ch):
            idx = ord(ch) - ord('a')
            return idx // 5, idx % 5

        r = c = 0
        res = []

        for ch in target:
            nr, nc = pos(ch)

            # Move up/left first (important for 'z')
            while r > nr:
                res.append('U')
                r -= 1
            while c > nc:
                res.append('L')
                c -= 1

            # Then move down/right
            while r < nr:
                res.append('D')
                r += 1
            while c < nc:
                res.append('R')
                c += 1

            res.append('!')

        return ''.join(res)