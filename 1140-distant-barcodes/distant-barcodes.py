from collections import Counter

class Solution:
    def rearrangeBarcodes(self, barcodes):
        count = Counter(barcodes)

        items = sorted(count.items(), key=lambda x: -x[1])

        n = len(barcodes)
        res = [0] * n

        idx = 0

        for num, freq in items:
            while freq > 0:
                res[idx] = num
                idx += 2

                if idx >= n:
                    idx = 1

                freq -= 1

        return res