class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        
        parent = list(range(26))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa = find(a)
            pb = find(b)

            if pa == pb:
                return

            if pa < pb:
                parent[pb] = pa
            else:
                parent[pa] = pb

        for a, b in zip(s1, s2):
            union(ord(a) - ord('a'), ord(b) - ord('a'))

        result = []

        for ch in baseStr:
            root = find(ord(ch) - ord('a'))
            result.append(chr(root + ord('a')))

        return "".join(result)