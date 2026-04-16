class Solution(object):
    def flipLights(self, n, presses):
        """
        :type n: int
        :type presses: int
        :rtype: int
        """
        if presses == 0:
            return 1

        n = min(n, 3)
        presses = min(presses, 3)

        seen = set()

        def press(state, op):
            res = list(state)

            if op == 0:  # all
                for i in range(len(res)):
                    res[i] ^= 1

            elif op == 1:  # even
                for i in range(1, len(res), 2):
                    res[i] ^= 1

            elif op == 2:  # odd
                for i in range(0, len(res), 2):
                    res[i] ^= 1

            else:  # 3k + 1
                for i in range(len(res)):
                    if (i + 1) % 3 == 1:
                        res[i] ^= 1

            return tuple(res)

        def dfs(state, p):
            if p == presses:
                seen.add(state)
                return

            for op in range(4):
                dfs(press(state, op), p + 1)

        start = tuple([1] * n)
        dfs(start, 0)

        return len(seen)