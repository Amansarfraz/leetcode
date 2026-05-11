class Solution(object):
    def largestComponentSize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        import math
        
        # DSU (Union Find)
        parent = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px
        
        # initialize parents
        for num in nums:
            parent[num] = num
        
        # factor map: prime -> first number seen
        prime_to_num = {}
        
        def get_primes(x):
            primes = set()
            d = 2
            while d * d <= x:
                while x % d == 0:
                    primes.add(d)
                    x //= d
                d += 1
            if x > 1:
                primes.add(x)
            return primes
        
        for num in nums:
            primes = get_primes(num)
            for p in primes:
                if p not in prime_to_num:
                    prime_to_num[p] = num
                else:
                    union(num, prime_to_num[p])
        
        count = defaultdict(int)
        ans = 0
        
        for num in nums:
            root = find(num)
            count[root] += 1
            ans = max(ans, count[root])
        
        return ans