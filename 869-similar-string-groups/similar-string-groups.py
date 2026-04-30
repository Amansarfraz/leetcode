class Solution(object):
    def numSimilarGroups(self, strs):
        
        parent = list(range(len(strs)))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pa] = pb
        
        # check similarity
        def similar(a, b):
            diff = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff += 1
                    if diff > 2:
                        return False
            return diff == 0 or diff == 2
        
        n = len(strs)
        
        for i in range(n):
            for j in range(i + 1, n):
                if similar(strs[i], strs[j]):
                    union(i, j)
        
        # count groups
        return len(set(find(i) for i in range(n)))