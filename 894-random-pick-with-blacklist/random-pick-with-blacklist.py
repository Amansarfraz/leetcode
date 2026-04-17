import random

class Solution(object):

    def __init__(self, n, blacklist):
        self.map = {}
        self.m = n - len(blacklist)
        
        blacklist_set = set(blacklist)
        
        last = n - 1
        
        for b in blacklist:
            if b < self.m:
                # find a valid number from the end
                while last in blacklist_set:
                    last -= 1
                
                self.map[b] = last
                last -= 1

    def pick(self):
        x = random.randint(0, self.m - 1)
        
        # remap if needed
        if x in self.map:
            return self.map[x]
        
        return x