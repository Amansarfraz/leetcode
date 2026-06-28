class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        perm = list(range(1, m + 1))
        ans = []

        for q in queries:
            idx = perm.index(q)
            ans.append(idx)
            perm.pop(idx)
            perm.insert(0, q)

        return ans