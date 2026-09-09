class Solution(object):
    def areConnected(self, n, threshold, queries):
        """
        :type n: int
        :type threshold: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # Edge case: If threshold is 0, all numbers share a divisor of 1, so everything is connected
        if threshold == 0:
            return [True] * len(queries)
            
        # Initialize DSU where each element is its own parent
        parent = list(range(n + 1))
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])  # Path compression
            return parent[i]
            
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j

        # Sieve-like approach to connect multiples of common divisors > threshold
        for divisor in range(threshold + 1, n + 1):
            for multiple in range(2 * divisor, n + 1, divisor):
                union(divisor, multiple)
                
        # Answer each query by checking if they share the same representative root
        ans = []
        for u, v in queries:
            ans.append(find(u) == find(v))
            
        return ans
