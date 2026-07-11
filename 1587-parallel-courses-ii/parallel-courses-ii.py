class Solution(object):
    def minNumberOfSemesters(self, n, relations, k):
        pre = [0] * n
        for u, v in relations:
            pre[v - 1] |= 1 << (u - 1)

        memo = {}

        def dfs(mask):
            if mask == (1 << n) - 1:
                return 0

            if mask in memo:
                return memo[mask]

            avail = 0
            for i in range(n):
                if (mask & (1 << i)) == 0 and (pre[i] & mask) == pre[i]:
                    avail |= 1 << i

            cnt = bin(avail).count("1")

            if cnt <= k:
                ans = 1 + dfs(mask | avail)
            else:
                ans = float("inf")
                sub = avail
                while sub:
                    if bin(sub).count("1") == k:
                        ans = min(ans, 1 + dfs(mask | sub))
                    sub = (sub - 1) & avail

            memo[mask] = ans
            return ans

        return dfs(0)