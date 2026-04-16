from collections import Counter

class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """

        sticker_counts = [Counter(s) for s in stickers]
        memo = {"": 0}

        def dfs(remain):
            if remain in memo:
                return memo[remain]

            target_count = Counter(remain)
            ans = float("inf")

            for sticker in sticker_counts:
                # optimization: skip useless stickers
                if sticker[remain[0]] == 0:
                    continue

                new_target = []

                for ch in target_count:
                    if target_count[ch] > 0:
                        diff = target_count[ch] - sticker.get(ch, 0)
                        if diff > 0:
                            new_target.extend([ch] * diff)

                new_target = "".join(new_target)

                res = dfs(new_target)
                if res != -1:
                    ans = min(ans, 1 + res)

            memo[remain] = -1 if ans == float("inf") else ans
            return memo[remain]

        return dfs(target)