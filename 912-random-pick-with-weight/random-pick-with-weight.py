import random
import bisect

class Solution(object):
    def __init__(self, w):
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total = total

    def pickIndex(self):
        target = random.randint(1, self.total)
        # Binary search
        index = bisect.bisect_left(self.prefix, target)
        return index