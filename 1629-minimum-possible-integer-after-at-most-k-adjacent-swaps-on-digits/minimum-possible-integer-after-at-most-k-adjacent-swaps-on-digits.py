from collections import deque

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i, delta):
        i += 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def query(self, i):
        s = 0
        i += 1
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


class Solution(object):
    def minInteger(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        n = len(num)
        pos = [deque() for _ in range(10)]

        for i, ch in enumerate(num):
            pos[int(ch)].append(i)

        bit = Fenwick(n)
        ans = []

        for _ in range(n):
            for d in range(10):
                if not pos[d]:
                    continue

                idx = pos[d][0]
                moved = bit.query(idx)
                cost = idx - moved

                if cost <= k:
                    k -= cost
                    ans.append(str(d))
                    bit.update(idx, 1)
                    pos[d].popleft()
                    break

        return "".join(ans)