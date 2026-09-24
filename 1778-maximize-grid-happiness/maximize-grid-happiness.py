class Solution(object):
    def getMaxGridHappiness(self, m, n, introvertsCount, extrovertsCount):
        """
        :type m: int
        :type n: int
        :type introvertsCount: int
        :type extrovertsCount: int
        :rtype: int
        """

        if m < n:
            m, n = n, m

        memo = {}
        pow3 = [1] * (n + 1)

        for i in range(1, n + 1):
            pow3[i] = pow3[i - 1] * 3

        # 0 = empty
        # 1 = introvert
        # 2 = extrovert

        def interaction(a, b):
            if a == 0 or b == 0:
                return 0

            if a == 1 and b == 1:
                return -60
            elif a == 1 and b == 2:
                return -10
            elif a == 2 and b == 1:
                return -10
            else:
                return 40

        def dp(pos, intro_left, extro_left, mask):
            if pos == m * n:
                return 0

            if intro_left == 0 and extro_left == 0:
                return 0

            state = (pos, intro_left, extro_left, mask)

            if state in memo:
                return memo[state]

            col = pos % n

            # Cell directly above
            up = (mask // pow3[n - 1]) % 3

            # Cell directly to the left
            left = mask % 3 if col > 0 else 0

            # Shift profile for next cell
            next_mask = (mask * 3) % pow3[n]

            # Leave current cell empty
            best = dp(
                pos + 1,
                intro_left,
                extro_left,
                next_mask
            )

            # Place introvert
            if intro_left > 0:
                gain = 120

                gain += interaction(1, up)
                gain += interaction(1, left)

                best = max(
                    best,
                    gain + dp(
                        pos + 1,
                        intro_left - 1,
                        extro_left,
                        next_mask + 1
                    )
                )

            # Place extrovert
            if extro_left > 0:
                gain = 40

                gain += interaction(2, up)
                gain += interaction(2, left)

                best = max(
                    best,
                    gain + dp(
                        pos + 1,
                        intro_left,
                        extro_left - 1,
                        next_mask + 2
                    )
                )

            memo[state] = best
            return best

        return dp(0, introvertsCount, extrovertsCount, 0)