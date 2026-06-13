class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        n = len(s)
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px

        for a, b in pairs:
            union(a, b)

        groups = {}

        for i in range(n):
            root = find(i)
            if root not in groups:
                groups[root] = []
            groups[root].append(s[i])

        for root in groups:
            groups[root].sort(reverse=True)

        res = []

        for i in range(n):
            root = find(i)
            res.append(groups[root].pop())

        return "".join(res)