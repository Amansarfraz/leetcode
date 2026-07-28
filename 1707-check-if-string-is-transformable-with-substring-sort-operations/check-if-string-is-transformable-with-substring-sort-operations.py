from collections import deque

class Solution(object):
    def isTransformable(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        pos = [deque() for _ in range(10)]

        for i, ch in enumerate(s):
            pos[int(ch)].append(i)

        for ch in t:
            d = int(ch)

            if not pos[d]:
                return False

            idx = pos[d][0]

            for smaller in range(d):
                if pos[smaller] and pos[smaller][0] < idx:
                    return False

            pos[d].popleft()

        return True