class Solution(object):
    def shortestSuperstring(self, words):
        n = len(words)

        # overlap[i][j]
        def calc(a, b):
            for k in range(min(len(a), len(b)), 0, -1):
                if a[-k:] == b[:k]:
                    return k
            return 0

        overlap = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    overlap[i][j] = calc(words[i], words[j])

        dp = [[float('inf')] * n for _ in range(1 << n)]
        parent = [[-1] * n for _ in range(1 << n)]

        for i in range(n):
            dp[1 << i][i] = len(words[i])

        for mask in range(1 << n):
            for i in range(n):
                if not (mask & (1 << i)):
                    continue
                for j in range(n):
                    if mask & (1 << j):
                        continue

                    nxt = mask | (1 << j)
                    cost = dp[mask][i] + len(words[j]) - overlap[i][j]

                    if cost < dp[nxt][j]:
                        dp[nxt][j] = cost
                        parent[nxt][j] = i

        # find best end
        mask = (1 << n) - 1
        last = min(range(n), key=lambda i: dp[mask][i])

        # reconstruct order
        path = []
        cur = last
        m = mask

        while cur != -1:
            path.append(cur)
            p = parent[m][cur]
            m ^= (1 << cur)
            cur = p

        path = path[::-1]

        # build answer
        ans = words[path[0]]
        for i in range(1, len(path)):
            ov = overlap[path[i-1]][path[i]]
            ans += words[path[i]][ov:]

        return ans