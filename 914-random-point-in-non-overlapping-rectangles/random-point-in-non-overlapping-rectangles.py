import random
import bisect

class Solution(object):

    def __init__(self, rects):
        self.rects = rects
        self.prefix = []
        total = 0
        
        # 🔥 build prefix sum of areas
        for x1, y1, x2, y2 in rects:
            area = (x2 - x1 + 1) * (y2 - y1 + 1)
            total += area
            self.prefix.append(total)
        
        self.total = total

    def pick(self):
        # 🔥 pick random point index
        k = random.randint(1, self.total)
        
        # find rectangle index
        idx = bisect.bisect_left(self.prefix, k)
        x1, y1, x2, y2 = self.rects[idx]
        
        # pick random point inside rectangle
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)
        
        return [x, y]