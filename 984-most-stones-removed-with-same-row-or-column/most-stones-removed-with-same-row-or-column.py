class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        
        parent = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent.setdefault(x, x)
            parent.setdefault(y, y)
            
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
        
        # connect row + col as nodes
        for x, y in stones:
            union(x, ~y)   # ~y used to separate row/col space
        
        # count components
        roots = set()
        for x, y in stones:
            roots.add(find(x))
            roots.add(find(~y))
        
        return len(stones) - len(roots)