import random

class Solution(object):

    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.map = {}
        self.total = m * n

    def flip(self):
        r = random.randint(0, self.total - 1)
        self.total -= 1
        
        # Get actual index
        x = self.map.get(r, r)
        
        # Swap with last available position
        self.map[r] = self.map.get(self.total, self.total)
        
        # Convert 1D index → 2D
        return [x // self.n, x % self.n]

    def reset(self):
        self.map.clear()
        self.total = self.m * self.n