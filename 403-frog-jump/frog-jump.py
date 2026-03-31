class Solution(object):
    def canCross(self, stones):
        stone_set = set(stones)
        dp = {stone: set() for stone in stones}
        dp[0].add(0)

        for stone in stones:
            for jump in dp[stone]:
                for step in [jump - 1, jump, jump + 1]:
                    if step > 0 and stone + step in stone_set:
                        dp[stone + step].add(step)

        return len(dp[stones[-1]]) > 0