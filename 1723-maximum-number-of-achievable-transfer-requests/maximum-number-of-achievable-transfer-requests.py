class Solution(object):
    def maximumRequests(self, n, requests):
        """
        :type n: int
        :type requests: List[List[int]]
        :rtype: int
        """
        balance = [0] * n
        m = len(requests)
        self.ans = 0

        def dfs(i, count):
            if i == m:
                if all(x == 0 for x in balance):
                    self.ans = max(self.ans, count)
                return

            # Skip current request
            dfs(i + 1, count)

            # Take current request
            frm, to = requests[i]
            balance[frm] -= 1
            balance[to] += 1

            dfs(i + 1, count + 1)

            # Backtrack
            balance[frm] += 1
            balance[to] -= 1

        dfs(0, 0)
        return self.ans