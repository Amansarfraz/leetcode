class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        rows = []

        for i, row in enumerate(mat):
            soldiers = sum(row)
            rows.append((soldiers, i))

        rows.sort()

        return [idx for _, idx in rows[:k]]