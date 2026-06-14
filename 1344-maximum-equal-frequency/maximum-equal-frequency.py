from collections import defaultdict

class Solution(object):
    def maxEqualFreq(self, nums):
        freq = defaultdict(int)
        count = defaultdict(int)

        res = 0
        maxF = 0

        for i, x in enumerate(nums):
            prev = freq[x]
            if prev > 0:
                count[prev] -= 1

            freq[x] += 1
            cur = freq[x]

            count[cur] += 1
            maxF = max(maxF, cur)

            n = i + 1

            # Case 1: all frequency 1
            if maxF == 1:
                res = n

            # Case 2: one number has freq maxF and others are maxF-1 or 0
            elif count[maxF] * maxF == n - 1 and count[1] == 1:
                res = n

            # Case 3: one number is at maxF, others at maxF-1
            elif count[maxF] == 1 and (count[maxF - 1] * (maxF - 1) + maxF == n):
                res = n

        return res