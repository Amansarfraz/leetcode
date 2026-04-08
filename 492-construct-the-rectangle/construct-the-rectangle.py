class Solution(object):
    def constructRectangle(self, area):
        import math
        
        w = int(math.sqrt(area))
        
        while area % w != 0:
            w -= 1
        
        return [area // w, w]