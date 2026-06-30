class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = list(str(num))

        # Create maximum number
        a = s[:]
        for ch in a:
            if ch != '9':
                target = ch
                a = ['9' if c == target else c for c in a]
                break
        maxNum = int("".join(a))

        # Create minimum number
        b = s[:]
        if b[0] != '1':
            target = b[0]
            b = ['1' if c == target else c for c in b]
        else:
            target = None
            for ch in b[1:]:
                if ch != '0' and ch != '1':
                    target = ch
                    break
            if target:
                b = ['0' if c == target else c for c in b]

        minNum = int("".join(b))

        return maxNum - minNum