class Solution(object):
    def nearestPalindromic(self, n):
        length = len(n)
        num = int(n)

        # Edge cases
        if num <= 10:
            return str(num - 1)
        if num == 11:
            return "9"

        # Helper: build palindrome from prefix
        def make_pal(prefix, odd):
            if odd:
                return prefix + prefix[-2::-1]
            return prefix + prefix[::-1]

        # Get prefix
        half_len = (length + 1) // 2
        prefix = int(n[:half_len])

        candidates = set()

        # base candidates: prefix -1, prefix, prefix +1
        for diff in [-1, 0, 1]:
            new_prefix = str(prefix + diff)
            if len(new_prefix) != len(str(prefix)):
                continue
            candidates.add(make_pal(new_prefix, length % 2))

        # edge cases like 999 -> 1001, 1000 -> 999
        candidates.add("9" * (length - 1))
        candidates.add("1" + ("0" * (length - 1)) + "1")

        candidates.discard(n)

        # find closest
        res = None
        min_diff = float("inf")

        for cand in candidates:
            if not cand:
                continue
            diff = abs(int(cand) - num)
            if diff < min_diff or (diff == min_diff and int(cand) < int(res)):
                min_diff = diff
                res = cand

        return res