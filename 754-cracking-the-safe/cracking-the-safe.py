class Solution(object):
    def crackSafe(self, n, k):
        seen = set()
        res = []
        
        def dfs(node):
            for x in map(str, range(k)):
                nei = node + x
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei[1:])
                    res.append(x)
        
        start = "0" * (n - 1)
        dfs(start)
        
        return "".join(res) + start   # 🔥 FIX HERE