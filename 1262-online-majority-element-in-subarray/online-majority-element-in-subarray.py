from collections import defaultdict
from bisect import bisect_left, bisect_right

class MajorityChecker(object):

    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        self.arr = arr
        self.n = len(arr)

        self.pos = defaultdict(list)
        for i, x in enumerate(arr):
            self.pos[x].append(i)

        self.seg = [None] * (4 * self.n)
        self._build(1, 0, self.n - 1)

    def _merge(self, a, b):
        if a[0] == b[0]:
            return (a[0], a[1] + b[1])

        if a[1] > b[1]:
            return (a[0], a[1] - b[1])

        return (b[0], b[1] - a[1])

    def _build(self, idx, l, r):
        if l == r:
            self.seg[idx] = (self.arr[l], 1)
            return

        m = (l + r) // 2
        self._build(idx * 2, l, m)
        self._build(idx * 2 + 1, m + 1, r)

        self.seg[idx] = self._merge(
            self.seg[idx * 2],
            self.seg[idx * 2 + 1]
        )

    def _query(self, idx, l, r, ql, qr):
        if ql <= l and r <= qr:
            return self.seg[idx]

        m = (l + r) // 2

        if qr <= m:
            return self._query(idx * 2, l, m, ql, qr)

        if ql > m:
            return self._query(idx * 2 + 1, m + 1, r, ql, qr)

        left_res = self._query(idx * 2, l, m, ql, qr)
        right_res = self._query(idx * 2 + 1, m + 1, r, ql, qr)

        return self._merge(left_res, right_res)

    def query(self, left, right, threshold):
        """
        :type left: int
        :type right: int
        :type threshold: int
        :rtype: int
        """
        candidate = self._query(1, 0, self.n - 1, left, right)[0]

        positions = self.pos[candidate]
        freq = bisect_right(positions, right) - bisect_left(positions, left)

        return candidate if freq >= threshold else -1


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left, right, threshold)